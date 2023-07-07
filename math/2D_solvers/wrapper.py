import sys
import subprocess
import solve_b
import json

sys.path.insert(0, "DSRI/2D/scraper/parse.py")
print(sys.path)
import parse


def solve(eqn: str) -> str:
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
    # No Milnor or Tjurina (returns vector []) => Milnor/Tjurina number is 0
    data["milnor"] = eval(output[1]) if len(output[1]) > 2 else 0
    data["tjurina"] = eval(output[2]) if len(output[2]) > 2 else 0
    homogenized = output[3]
    singular_points = output[4]
    print(singular_points)
    # data["sings"] = solve_b.solve_singularities(homogenized, singular_points)
    # data["mults"] = solve_b.solve_multiplicities(homogenized, singular_points)
    print(output)
    return data


def main():
    try:
        eqn = sys.argv[1]
        if "^" in eqn:
            print(solve(eqn))
        else:
            pr
    except IndexError:
        print("Enter the equation to solve invariants for.")


if __name__ == "__main__":
    main()
