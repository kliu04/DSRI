def add_braces_to_exponents(eqn: str) -> str:
    eqn = eqn.replace("*", "")
    lis = []
    flag = False
    for i, e_indexc in enumerate(eqn):
        if e_indexc == "^":
            lis.append(i + len(lis))
            flag = True
        elif flag and not e_indexc.isnumeric():
            lis.append(i - 1 + len(lis))
            flag = False
    if flag:
        lis.append(len(eqn) - 1 + len(lis))

    alt = True
    for eqn_index in lis:
        if alt:
            eqn = eqn[: eqn_index + 1] + "{" + eqn[eqn_index + 1 :]
            alt = False
        else:
            eqn = eqn[: eqn_index + 1] + "}" + eqn[eqn_index + 1 :]
            alt = True
    return eqn


add_braces_to_exponents("5x^12+6y^3")
