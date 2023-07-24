import sys
import subprocess
import solve_b
import json
import parse


def solve(eqn: str) -> dict:
    """Solve for invariants of a 2D curve given equation as argument."""
    data = {}
    try:
        output = (
            # Run Macaulay2 script (need primary decomposition to get all singular points)
            subprocess.run(
                ["M2", "--script", "./math/2D_solvers/solve_a.m2", eqn],
                capture_output=True,
                text=True,
            )
            .stdout.strip()
            .split("\n")
        )
    except Exception as e:
        print("An error occurred when trying to run M2:", e)
        return data
    data["eqn"] = eqn
    data["degree"] = int(output[0])
    homogenized = output[1]
    singular_points = output[2]
    data["sings"], data["sings_latex"] = solve_b.solve_singularities(singular_points)
    data["mults"] = solve_b.solve_multiplicities(homogenized, data["sings"])
    data["milnor"] = solve_b.solve_milnor(output[3], output[4], data["sings"])
    data["tjurina"] = solve_b.solve_tjurina(output[5], output[6], data["sings"])

    data["arith_genus"] = solve_b.solve_arith_genus(data["degree"])
    data["delta"] = solve_b.solve_delta(data["mults"])
    data["geo_genus"] = solve_b.solve_geo_genus(data["arith_genus"], data["delta"])
    data["branching"] = solve_b.solve_branching(data["milnor"], data["delta"])
    return data


def main():
    try:
        eqn = sys.argv[1]
        # Hacky way to differentiate properly formatted from katie
        if "^" in eqn:
            print(solve(eqn))
        else:
            # parse if from katie's site
            print(solve(parse.parse(eqn)))
    except IndexError:
        print("Enter the equation to solve invariants for.")


if __name__ == "__main__":
    main()
