import json
import wrapper
from parse import parse


def main():
    surfaces = []
    with open("math/3D_solvers/surfaces.json", "r") as f:
        surfaces = json.load(f)
        for i, surface in enumerate(surfaces):
            try:
                data = wrapper.solve(parse(surface["eqn"]))
                surface = surface | data
                surface["sings"] = str(surface["sings"])
                surfaces[i] = surface
            except Exception as e:
                print(e, surface)

    with open("math/3D_solvers/surfaces.json", "w") as f:
        json.dump(surfaces, f, indent=4)


if __name__ == "__main__":
    main()
