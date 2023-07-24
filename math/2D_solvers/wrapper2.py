import sys
import subprocess
import json
import parse
import solve_b
from sympy import I


def solve(eqn: str) -> dict:
    """Solve for invariants of a 2D curve given as argument."""
    data = {}
    try:
        output = (
            # Run Macaulay2 script (need primary decomposition to get all singular points)
            subprocess.run(
                ["M2", "--script", "./math/2D_solvers/keratoid.m2", eqn],
                capture_output=True,
                text=True,
            )
            .stdout.strip()
            .split("\n")
        )

    except Exception as e:
        print("An error occurred when trying to run M2:", e)
        return data
    # data["sings"] = [(0, 1, 1), (0, -1, 1), (1, 0, 1), (-1, 0, 1)]
    # data["sings"] = [(0, 0, 1), (101, 0, 1), (I, 1, 0), (-I, 1, 0)]
    # data["sings"] = [(0, 0, 1), (1, -1, 1), (1, 1, 1)]
    # data["sings"] = [(0, 0, 1), (0, 1, 0)]
    data["sings"] = [(0, 0, 1)]

    solve_b.solve_milnor(output[1], output[0], data["sings"])

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
