from sympy import solve, Symbol


def main():
    x = Symbol("x", real=True)
    y = Symbol("y", real=True)
    # homogenized with z set to 0 already
    f = x**5
    sols = solve(f, dict=True)
    sols = [sol for sol in sols if sol[x].is_real]
    for sol in sols:
        sol[x] = sol[x].subs(y, 1)
        print([sol[x], 1, 0])


if __name__ == "__main__":
    main()
