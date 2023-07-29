import requests
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
import sys
import parse
import json
import wrapper


URL = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html"
BASE = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/"


def run_solvers(data: dict) -> dict:
    eqn = data["eqn"]
    data = data | wrapper.solve(eqn)
    del data["sings"]
    return data


def parse_sublink(link: str) -> dict:
    page = requests.Session().get(link)
    soup = BeautifulSoup(page.text, "lxml")
    data = {}
    text = soup.get_text()
    eqn = text[text.find("Equation:") + 10 : text.find("Degree:")].replace("\n", "")
    eqn = eqn[: eqn.rfind("=")].strip()
    eqn = parse.parse(eqn)
    data["title"] = soup.title.string.replace("\u2019", "'")
    data["eqn"] = eqn
    return run_solvers(data)


def main():
    sys.setrecursionlimit(10000)

    a_tags = SoupStrainer("a")
    page = requests.Session().get(URL)
    soup = BeautifulSoup(page.text, "lxml", parse_only=a_tags)
    links = soup.find_all("a")
    links = links[: len(links) - 3]
    links = [link.get("href") for link in links]

    all_curves = []
    # 62 threads
    with Pool(62) as p:
        all_curves = p.map(parse_sublink, [BASE + sublink for sublink in links])
    # all_curves = [str(curve) for curve in all_curves]
    # for it in map(parse_sublink, [BASE + sublink for sublink in links]):
    #     all_curves.append(it)
    try:
        with open("math/2D_solvers/parsed_data.json", "w") as f:
            json.dump(all_curves, f, indent=4)
    except:
        print("Convert to serializeable!")
        all_curves = [{key: str(val) for key, val in dict.items()} for dict in list]
        with open("math/2D_solvers/parsed_data.json", "w") as f:
            json.dump(all_curves, f, indent=4)


if __name__ == "__main__":
    main()
