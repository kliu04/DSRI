import json


def add_braces_to_exponents(eqn: str) -> str:
    pass


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
            for r in replace:
                old = rf"[[ {r} ]]"
                new = str(curve[r])
                # Singularity conversion
                new = new.replace("'", "")
                # Eqn conversion
                # new = new.replace("*", "")
                site = site.replace(old, new)
            with open("2D/" + curve["title"] + ".html", "w") as f:
                f.write(site)
        except KeyError:
            pass
        except FileNotFoundError:
            pass  # 2D_sites/Lemniscate of Gerono/ Eight Curve.html (annoying slash)
        except:
            print("Error!!!", curve)
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


#     <tr>
#     <td>\(3\)</td>
#     <td><a href="./cayley_surface.html">Cayley's Surface</a></td>
#     <td>\(x^2+y^2+z^2+x^2z-y^2z-1=0\)</td>
#     </tr>

if __name__ == "__main__":
    main()
