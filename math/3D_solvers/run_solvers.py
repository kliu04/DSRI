import json
import wrapper
from parse import parse
import signal


def timeout(signum, frame):
    raise TimeoutError


def main():
    surfaces = []
    # timeout if computations take too long
    signal.signal(signal.SIGALRM, timeout)
    with open("math/3D_solvers/surfaces.json", "r") as f:
        # Load title and eqn
        surfaces = json.load(f)
        for i, surface in enumerate(surfaces):
            signal.alarm(60)
            try:
                # parse eqn if needed
                parsed = parse(surface["eqn"])
                print(surface["title"], parsed)
                surface["eqn"] = parsed
                # solve invars
                data = wrapper.solve(parsed)
                # merge resulting dict
                surface = surface | data
                surface["sings"] = str(surface["sings"])
                # update list
                surfaces[i] = surface
            except TimeoutError:
                print("Skipping " + surface["title"])
                continue
            except Exception as e:
                print(e, surface)
    signal.alarm(0)
    with open("math/3D_solvers/surfaces.json", "w") as f:
        json.dump(surfaces, f, indent=4)


if __name__ == "__main__":
    main()
