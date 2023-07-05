from sympy import solve, im, poly, expand, sqrt
from sympy.abc import x, y, z, I
from pathlib import Path
from sympy.parsing.sympy_parser import parse_expr


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
                system.append(parse_expr(token))

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
        # f.write("Singularities:\n")
        # print("Singularities:")
        output = []
        for i, v in enumerate(sols):
            if v[z] != 0:
                v[x] /= v[z]
                v[y] /= v[z]
                v[z] = 1
            elif v[y] != 0:
                v[x] /= v[y]
                v[y] = 1
            else:
                # Sing is of form (x, 0, 0)
                v[x] = 1
            sol = (v[x], v[y], v[z])
            sols[i] = sol

        # Remove duplicates
        sols = list(dict.fromkeys(sols))

        for sol in sols:
            # f.write(str(sol) + "\n")
            output.append(list(sol))
            # print(str(sol))
        print(output)

        # Multiplicities
        mults = []

        for sol in sols:
            # shift solution
            shifted = ""
            try:
                # rework this code
                shifted = eqn.replace("x", "(x-" + str(sol[0]) + ")")
                shifted = shifted.replace("y", "(y-" + str(sol[1]) + ")")
                shifted = shifted.replace("z", "(z-" + str(sol[2]) + ")")

                # if im(sol[0]) == 0:
                #     if sol[0] >= 0:
                #         shifted = eqn.replace("x", "(x-" + str(sol[0]) + ")")
                #     else:
                #         shifted = eqn.replace("x", "(x+" + str(-1 * sol[0]) + ")")
                # else:
                #     if im(sol[0]) >= 0:
                #         shifted = eqn.replace("x", "(x-" + str(sol[0]) + ")")
                #     else:
                #         shifted = eqn.replace("x", "(x+" + str(-1 * sol[0]) + ")")
                # if im(sol[1]) == 0:
                #     if sol[1] >= 0:
                #         shifted = shifted.replace("y", "(y-" + str(sol[1]) + ")")
                #     else:
                #         shifted = shifted.replace("y", "(y+" + str(-1 * sol[1]) + ")")
                # else:
                #     if im(sol[1]) >= 0:
                #         shifted = shifted.replace("y", "(y-" + str(sol[1]) + ")")
                #     else:
                #         shifted = shifted.replace("y", "(y+" + str(-1 * sol[1]) + ")")
                # if im(sol[2]) == 0:
                #     if sol[2] >= 0:
                #         shifted = shifted.replace("z", "(z-" + str(sol[2]) + ")")
                #     else:
                #         shifted = shifted.replace("z", "(z+" + str(-1 * sol[2]) + ")")
                # else:
                #     if im(sol[2]) >= 0:
                #         shifted = shifted.replace("z", "(z-" + str(sol[2]) + ")")
                #     else:
                #         shifted = shifted.replace("z", "(z+" + str(-1 * sol[2]) + ")")

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
                    # degree of each variable
                    for d_v in degrees:
                        total_degree += d_v
                    # ignore cnst term
                    if total_degree == 0:
                        continue
                    degree_list.append(total_degree)
                mults.append(min(degree_list))
            except:
                print(sol, "Error!!!")

        # f.write("Multiplicities:\n")
        # f.write(str(mults))
        # print("Multiplicities:")
        print(str(mults))

        # f.write("\n")


if __name__ == "__main__":
    main()
