from sympy import solve
from sympy.abc import w, x, y, z
from pathlib import Path


def main():
    # TODO: fix for server directory
    path = Path("computations")
    sols = []
    eqn = ""
    with open(path / "mults.txt", "r", encoding="utf-8") as f:
        for line in f:
            # Get rid of useless characters
            line = line.strip("\n")
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace(" ", "")
            line = line.replace("^", "**")

            tokens = line.split(",")

            # homogenized equation
            if len(tokens) == 1:
                eqn = line.replace("**", "^")
                continue

            missing = set()
            if "w" not in line:
                missing.add(w)
            if "x" not in line:
                missing.add(x)
            if "y" not in line:
                missing.add(y)
            if "z" not in line:
                missing.add(z)

            if len(tokens) == 2:
                system = []
                system.append(eval(tokens[0]))
                system.append(eval(tokens[1]))
                sol = solve(
                    system,
                    # don't solve for the missing variable
                    list({w, x, y, z} - missing),
                    dict=True,
                )

            elif len(tokens) == 3:
                system = []
                system.append(eval(tokens[0]))
                system.append(eval(tokens[1]))
                system.append(eval(tokens[2]))

                sol = solve(
                    system,
                    list({w, x, y, z} - missing),
                    dict=True,
                )

            for item in missing:
                sol[0][item] = 1
            sols.append(sol)

    # flatten list
    sols = [item for sublist in sols for item in sublist]
    with open(path / "mults_solution.txt", "w", encoding="utf-8") as f:
        # turn dicts to tuples
        for i, v in enumerate(sols):
            sol = (v[w], v[x], v[y], v[z])
            sols[i] = sol

        # Remove duplicates
        sols = list(dict.fromkeys(sols))

        for sol in sols:
            f.write(str(sol) + "\n")

    with open("calc_mults.m2", "w", encoding="utf-8") as f:
        f.write("{\n")
        for sol in sols:
            shifted = ""
            if sol[0] >= 0:
                shifted = eqn.replace("w", "(w-" + str(sol[0]) + ")")
            else:
                shifted = eqn.replace("w", "(w+" + str(-1 * sol[0]) + ")")
            if sol[1] >= 0:
                shifted = shifted.replace("x", "(x-" + str(sol[1]) + ")")
            else:
                shifted = shifted.replace("x", "(x+" + str(-1 * sol[1]) + ")")
            if sol[2] >= 0:
                shifted = shifted.replace("y", "(y-" + str(sol[2]) + ")")
            else:
                shifted = shifted.replace("y", "(y+" + str(-1 * sol[2]) + ")")
            if sol[3] >= 0:
                shifted = shifted.replace("z", "(z-" + str(sol[3]) + ")")
            else:
                shifted = shifted.replace("z", "(z+" + str(-1 * sol[3]) + ")")
            f.write("degree tangentCone ideal (" + shifted + ")")
            if sol != sols[-1]:
                f.write(",\n")
            else:
                f.write("\n")
        f.write("}")


if __name__ == "__main__":
    main()
