import requests
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
import sys
import parse
import json
import math

URL = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html"
BASE = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/"

# Hacky solution
sys.path.insert(0, "/home/wevie/DSRI/math/2D_solvers")
import wrapper


def run_solvers(data: dict) -> dict:
    eqn = data["eqn"]
    # print(eqn)
    # print(data | wrapper.solve(eqn))
    return data | wrapper.solve(eqn)


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

    # for it in map(parse_sublink, [BASE + sublink for sublink in links]):
    #     all_curves.append(it)

    with open("2D/scraper/parsed_data.json", "w") as f:
        json.dump(all_curves, f, indent=4)


if __name__ == "__main__":
    main()
