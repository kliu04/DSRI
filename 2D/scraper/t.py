def a(eqn):
    new = ""
    for i, v in enumerate(eqn[:]):
        if v == "*":
            if eqn[i - 1].isalpha() or eqn[i + 1].isalpha():
                continue
        new += v
    return new


print(a("x^4-101^2*x^2+101^2*y^2"))
