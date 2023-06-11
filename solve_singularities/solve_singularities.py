from sympy import solve
from sympy.abc import x, y, z

from pathlib import Path


def main():
    # TODO: fix for server directory
    path = Path("solve_singularities")
    sols = []
    with open(path / "file.txt", "r", encoding="utf-8") as f:
        for line in f:
            # Get rid of useless characters
            line = line.strip("\n")
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace(" ", "")
            line = line.replace("^", "**")

            tokens = line.split(",")

            if len(tokens) == 2:
                if "x" not in tokens:
                    missing = x
                elif "y" not in tokens:
                    missing = y
                elif "z" not in tokens:
                    missing = z
                else:
                    raise NotImplementedError

                system = []
                system.append(eval(tokens[0]))
                system.append(eval(tokens[1]))
                sol = solve(
                    system,
                    # don't solve for the missing variable
                    list({x, y, z} - {missing}),
                    dict=True,
                )

                # re-add the missing variable
                sol[0][missing] = 1
                sols.append(sol)

            elif len(tokens) == 3:
                system = []
                system.append(eval(tokens[0]))
                system.append(eval(tokens[1]))
                system.append(eval(tokens[2]))

                # solve system of 3 eqs
                sols.append(
                    solve(
                        system,
                        [x, y, z],
                        dict=True,
                    )
                )

            else:
                raise NotImplementedError

    # flatten list
    sols = [item for sublist in sols for item in sublist]

    with open(path / "solutions.txt", "w", encoding="utf-8") as f:
        # for item in sols:
        #     sol = []
        #     sol.append(item[x])
        #     sol.append(item[y])
        #     sol.append(item[z])
        #     f.write(str(sol) + "\n")

        # turn dicts to tuples
        for i, v in enumerate(sols):
            sol = (v[x], v[y], v[z])
            sols[i] = sol

        # Remove duplicates
        sols = list(dict.fromkeys(sols))

        for sol in sols:
            f.write(str(sol) + "\n")


if __name__ == "__main__":
    main()
