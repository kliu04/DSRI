import json
import wrapper
from parse import parse


def main():
    surfaces = []
    with open("math/3D_solvers/surfaces.json", "r") as f:
        surfaces = json.load(f)
        for i, surface in enumerate(surfaces):
            data = wrapper.solve(parse(surface["eqn"]))
            surface = surface | data
            surface["sings"] = str(surface["sings"])
            surfaces[i] = surface
    with open("math/3D_solvers/surfaces.json", "w") as f:
        json.dump(surfaces, f, indent=4)


if __name__ == "__main__":
    main()
