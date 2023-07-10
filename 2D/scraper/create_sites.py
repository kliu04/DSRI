import json


def add_braces_to_exponents(eqn: str) -> str:
    """Convert eqn string to have braces for exponents (e.g., 5x^12 + 6y^3 -> 5x^{12} + 6y^{3})"""
    eqn = eqn.replace("*", "")
    # index of all places to insert braces
    lis = []
    flag = False
    for i, e_indexc in enumerate(eqn):
        # start left bracket
        if e_indexc == "^":
            # add len here because everytime a new character is inserted string length increments
            lis.append(i + len(lis))
            flag = True
        elif flag and not e_indexc.isnumeric():
            lis.append(i - 1 + len(lis))
            flag = False
    if flag:
        lis.append(len(eqn) - 1 + len(lis))

    # alternate left and right braces
    alt = True
    for eqn_index in lis:
        if alt:
            eqn = eqn[: eqn_index + 1] + "{" + eqn[eqn_index + 1 :]
            alt = False
        else:
            eqn = eqn[: eqn_index + 1] + "}" + eqn[eqn_index + 1 :]
            alt = True
    return eqn


def main():
    curves = []
    template = ""
    with open("2D/scraper/parsed_data.json", "r") as f:
        curves = json.load(f)
    with open("2D/scraper/template.txt", "r") as f:
        template = f.read()

    for curve in curves:
        site = template[:]
        replace = [
            "title",
            "eqn",
            "degree",
            "milnor",
            "tjurina",
            "sings",
            "mults",
            "arith_genus",
            "delta",
            "geo_genus",
            "branching",
        ]
        try:
            # replace template info ([[x]]) with json_data[x]
            for r in replace:
                # use raw string here since some curves have / in name (path seperator)
                old = rf"[[ {r} ]]"
                new = str(curve[r])
                # Singularity conversion
                new = new.replace("'", "")
                # Eqn conversion
                if r == "eqn":
                    new = add_braces_to_exponents(new)
                site = site.replace(old, new)
            with open("2D/" + curve["title"] + ".html", "w") as f:
                f.write(site)
        # some curves may not have all invariants for whatever reason
        except KeyError:
            pass
        except:
            print("Error!!!", curve)

    # make main index page
    with open("2D/scraper/index_template.txt", "r") as f:
        template = f.readlines()
    index = 0
    for i, v in enumerate(template):
        if '<tbody class="table-group-divider">' in v:
            index = i + 1
            break
    for i, v in enumerate(curves):
        try:
            template.insert(index + 5 * i, "          <tr>\n")
            template.insert(
                index + 5 * i + 1, "            <td>\(%d\)</td>\n" % v["degree"]
            )
            template.insert(
                index + 5 * i + 2,
                '            <td><a href="./%s.html">%s</a></td>\n'
                % (v["title"], v["title"]),
            )
            template.insert(
                index + 5 * i + 3,
                "            <td>\(%s\)</td>\n" % v["eqn"].replace("*", ""),
            )
            template.insert(index + 5 * i + 4, "          </tr>\n")
        except:
            continue
    with open("2D/index.html", "w") as f:
        f.write("".join(template))


if __name__ == "__main__":
    main()
