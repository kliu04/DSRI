import json


def main():
    curves = []
    template = ""
    with open("parsed_data.txt", "r") as f:
        curves = json.load(f)
    with open("2D_sites/template.txt", "r") as f:
        template = f.read()
    for curve in curves:
        site = template[:]
        replace = ["title", "eqn", "degree", "milnor", "tjurina", "sings", "mults"]
        try:
            for r in replace:
                old = f"[[ {r} ]]"
                site = site.replace(old, str(curve[r]))
            with open("2D_sites/" + curve["title"] + ".html", "w") as f:
                f.write(site)
        except KeyError:
            pass
        except FileNotFoundError:
            pass  # 2D_sites/Lemniscate of Gerono/ Eight Curve.html (annoying slash)
        except:
            print("Error!!!", curve)


if __name__ == "__main__":
    main()
