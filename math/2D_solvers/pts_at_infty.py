from sympy import solve, Symbol


def main():
    x = Symbol("x", real=True)
    y = Symbol("y", real=True)
    f = x**2
    sols = solve(f, dict=True)
    sols = [sol for sol in sols if sol[x].is_real]
    for sol in sols:
        sol[x] = sol[x].subs(y, 1)
        print([sol[x], 1, 0])


if __name__ == "__main__":
    main()
