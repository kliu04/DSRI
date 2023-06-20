from sympy import solve, im, poly, expand, sqrt
from sympy.abc import x, y, z, I
from pathlib import Path


def main():
    # TODO: fix for server directory
    path = Path().resolve()
    sols = []
    eqn = ""
    with open(path / "2d_to_solve.txt", "r", encoding="utf-8") as f:
        for line in f:
            # Get rid of formatting characters
            line = line.strip("\n")
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace(" ", "")
            line = line.replace("^", "**")

            tokens = line.split(",")

            if len(tokens) == 1:
                eqn = line.replace("**", "^")
                continue

            missing = set()
            if "x" not in line:
                missing.add(x)
            if "y" not in line:
                missing.add(y)
            if "z" not in line:
                missing.add(z)

            system = []
            for token in tokens:
                system.append(eval(token))

            sol = solve(
                system,
                dict=True,
            )
            for item in missing:
                for j in range(len(sol)):
                    sol[j][item] = 1
                    sols.append(sol[j])

    with open(path / "2d_solutions.txt", "a", encoding="utf-8") as f:
        # turn dicts to tuples
        f.write("Singularities:\n")
        for i, v in enumerate(sols):
            sol = (v[x], v[y], v[z])
            sols[i] = sol

        # Remove duplicates
        sols = list(dict.fromkeys(sols))

        for sol in sols:
            f.write(str(sol) + "\n")

        # Multiplicities
        mults = []

        for i, v in enumerate(sols):
            sol = list(v)
            if sol[2] != 0:
                sol[0] /= sol[2]
                sol[1] /= sol[2]
                sol[2] = 1
            elif sol[1] != 0:
                sol[0] /= sol[1]
                sol[1] = 1
            elif sol[0] != 0:
                # should always trigger because (0, 0, 0) is imposible
                v[x] = 1
            else:
                raise ValueError
            sols[i] = sol

        for sol in sols:
            # shift solution
            shifted = ""
            if im(sol[0]) == 0:
                if sol[0] >= 0:
                    shifted = eqn.replace("x", "(x-" + str(sol[0]) + ")")
                else:
                    shifted = eqn.replace("x", "(x+" + str(-1 * sol[0]) + ")")
            else:
                if im(sol[0]) >= 0:
                    shifted = eqn.replace("x", "(x-" + str(sol[0]) + ")")
                else:
                    shifted = eqn.replace("x", "(x+" + str(-1 * sol[0]) + ")")
            if im(sol[1]) == 0:
                if sol[1] >= 0:
                    shifted = shifted.replace("y", "(y-" + str(sol[1]) + ")")
                else:
                    shifted = shifted.replace("y", "(y+" + str(-1 * sol[1]) + ")")
            else:
                if im(sol[1]) >= 0:
                    shifted = shifted.replace("y", "(y-" + str(sol[1]) + ")")
                else:
                    shifted = shifted.replace("y", "(y+" + str(-1 * sol[1]) + ")")
            if im(sol[2]) == 0:
                if sol[2] >= 0:
                    shifted = shifted.replace("z", "(z-" + str(sol[2]) + ")")
                else:
                    shifted = shifted.replace("z", "(z+" + str(-1 * sol[2]) + ")")
            else:
                if im(sol[2]) >= 0:
                    shifted = shifted.replace("z", "(z-" + str(sol[2]) + ")")
                else:
                    shifted = shifted.replace("z", "(z+" + str(-1 * sol[2]) + ")")

            shifted = shifted.replace("^", "**")

            # Get terms of polynominal
            # print(poly(expand(shifted)))
            # print(poly(expand(shifted)).terms())

            # degree of all terms
            degree_list = []
            # cannot break as planned here since terms are not sorted by degree but by variable
            for term in reversed(poly(expand(shifted)).terms()):
                total_degree = 0
                # degree of current term
                degrees = term[0]
                # ignore constant term
                if not all(degree == 0 for degree in degrees):
                    # degree of each variable
                    for d_v in degrees:
                        total_degree += d_v
                degree_list.append(total_degree)
            mults.append(min(degree_list))

        f.write("Multiplicities:\n")
        f.write(str(mults))
        f.write("\n")


if __name__ == "__main__":
    main()
