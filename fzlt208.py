
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    r = requests.get(
        "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
    html = r.text

    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all(class_="content-section"):
        for b in a.find_all("p"):
            print(b.text)
