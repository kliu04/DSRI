import requests
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
import sys
import parse
import json
import subprocess
import pathlib
import math

URL = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html"
BASE = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/"


def convert_mults_to_list(s: str) -> list:
    # okay if there are no fractional/non-natural multiplicities
    # len("[]")
    if len(s) == 2:
        return None
    return eval(s)


def convert_sings_to_list(s: str) -> list:
    if len(s) == 2:
        return None
    lis = s.split(",")
    ignore = "[] "
    parsed = []
    table = dict.fromkeys(map(ord, ignore), None)
    t = lambda x: x.translate(table)
    for i in range(0, len(lis), 3):
        parsed.append([t(lis[i]), t(lis[i + 1]), t(lis[i + 2])])
    return parsed


def run_solvers(data: dict) -> dict:
    # data = json.loads(data)
    eqn = data["eqn"]

    path = str(pathlib.Path().resolve() / "2d_run.sh")
    output = ""
    try:
        output = subprocess.run(
            f"bash {path} {eqn}",
            capture_output=True,
            shell=True,
            # timeout=30,
            text=True,
        ).stdout
        output = output.strip()
        output = output.split("\n")
        data["degree"] = int(output[0])
        if len(sorted(eval(output[1]))) == 0:
            data["milnor"] = 0
        else:
            data["milnor"] = sorted(eval(output[1]))
        if len(sorted(eval(output[2]))) == 0:
            data["tjurina"] = 0
        else:
            data["tjurina"] = sorted(eval(output[2]))
        data["sings"] = convert_sings_to_list(output[3])
        data["mults"] = convert_mults_to_list(output[4])
    except:
        # print(data, output)
        print(data, output)
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
    # 62 threads
    # with Pool(62) as p:
    #     pprint(p.map(parse_sublink, [BASE + sublink for sublink in links]))
    all_curves = []
    for it in map(parse_sublink, [BASE + sublink for sublink in links]):
        all_curves.append(it)
    all_curves = json.dumps(all_curves, indent=4)

    with open("parsed_data.txt", "w") as f:
        f.write(all_curves)


if __name__ == "__main__":
    main()
