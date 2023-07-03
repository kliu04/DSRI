import requests
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
import sys
import parse
import json
import os

URL = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html"
BASE = "https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/"


def parse_sublink(link: str):
    page = requests.Session().get(link)
    soup = BeautifulSoup(page.text, "lxml")
    data = {}
    eqn = (
        soup.get_text()[page.text.find("Equation:") + 10 : page.text.find("Degree:")]
        .strip()
        .replace("\n", "")
        .replace(" = 0", "")
    )
    # Hacky fix
    data["title"] = soup.title.string.replace("\u2019", "'").replace("\\", "")
    # eqn = parse.parse(eqn)
    print(eqn)
    data["eqn"] = eqn
    json_data = json.dumps(data)

    return json_data


def main():
    sys.setrecursionlimit(10000)

    a_tags = SoupStrainer("a")
    page = requests.Session().get(URL)
    soup = BeautifulSoup(page.text, "lxml", parse_only=a_tags)
    links = soup.find_all("a")
    links = links[: len(links) - 3]
    links = [link.get("href") for link in links]
    # 62 threads
    with Pool(62) as p:
        print(p.map(parse_sublink, [BASE + sublink for sublink in links]))


if __name__ == "__main__":
    main()
