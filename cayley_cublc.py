from sympy import S, solve, solveset, nsolve
from sympy.abc import x, y, z

print(
    solve(
        -5
        * (x**2 * y + x**2 * z + y**2 * x + y**2 * z + z**2 * y + z**2 * x)
        + 2 * (x * y + x * z + y * z),
        z,
        dict=True,
    )
)

print(
    solveset(
        -5
        * (x**2 * y + x**2 * z + y**2 * x + y**2 * z + z**2 * y + z**2 * x)
        + 2 * (x * y + x * z + y * z),
        z,
        domain=S.Reals,
    )
)

# z = f(x, y)
# or
# fix z to be constant and iterate through all values of z
