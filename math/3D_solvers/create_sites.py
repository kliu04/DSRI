import json


def parse_for_latex(eqn: str) -> str:
    """Convert string to be properly formatted for latex (e.g., 5*6^2*x^12 + 6*y^3 -> 5 \cdot 6^{2}x^{12} + 6y^{3})"""
    # eqn = eqn.replace("sqrt", "\sqrt")
    # eqn = eqn.replace("I", "i")
    # eqn = eqn.replace("**", "^")
    # remove excess multiplication signs
    parsed = ""
    for i, v in enumerate(eqn):
        if v == "*":
            if eqn[i + 1].isnumeric():
                parsed += " \cdot "
            continue
        parsed += v
    eqn = parsed
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
    surfaces = []
    links = []
    template = ""
    with open("math/3D_solvers/surfaces.json", "r") as f:
        surfaces = json.load(f)
    with open("math/3D_solvers/links.json", "r") as f:
        links = json.load(f)
    with open("math/3D_solvers/template.txt", "r") as f:
        template = f.read()

    for surface in surfaces:
        site = template[:]
        replace = [
            "title",
            "eqn",
            "degree",
            "milnor",
            "tjurina",
            "sings_latex",
            "mults",
        ]
        try:
            # replace template info ([[x]]) with json_data[x]
            for r in replace:
                field = rf"[[ {r} ]]"
                data = str(surface[r])
                # Singularity conversion to get rid of string
                if r == "sings":
                    data = data.replace("'", "")
                # Eqn conversion
                if r == "eqn":
                    data = parse_for_latex(data)
                    surface["eqn"] = data
                if r == "title":
                    surface["title"] = surface["title"].replace("/ ", "_")
                site = site.replace(field, data)
            index = site.find('<ul class="list-group">')
            index += len('<ul class="list-group">')
            for item in links:
                if item["title"] == surface["title"]:
                    for link in item["links"]:
                        site = (
                            site[:index]
                            + f'\n          <li class="list-group-item">\n            <a href="{link}">{link}</a></li>\n'
                            + site[index:]
                        )
            with open(rf"3D/{surface['title']}.html", "w") as f:
                f.write(site)
        # some surfaces may not have all invariants
        except KeyError:
            pass
        except Exception as e:
            print("Error!!!", surface, e)

    # make main index page
    with open("math/3D_solvers/index_template.txt", "r") as f:
        template = f.readlines()
    index = 0
    for i, v in enumerate(template):
        if '<tbody class="table-group-divider">' in v.strip():
            index = i + 1
            break
    for i, v in enumerate(surfaces):
        try:
            template.insert(index + 5 * i, "          <tr>\n")
            template.insert(
                index + 5 * i + 1, "            <td>\(%s\)</td>\n" % v["degree"]
            )
            template.insert(
                index + 5 * i + 2,
                '            <td><a href="./%s.html">%s</a></td>\n'
                % (v["title"], v["title"]),
            )
            template.insert(
                index + 5 * i + 3,
                "            <td>\(%s\)</td>\n" % v["eqn"],
            )
            template.insert(index + 5 * i + 4, "          </tr>\n")
        except Exception as e:
            continue
    with open("3D/index.html", "w") as f:
        f.write("".join(template))


if __name__ == "__main__":
    main()
