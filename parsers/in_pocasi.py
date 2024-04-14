from abc import ABC
import bs4
import requests

import generic_parser
from generic_parser import GenericParser, ScrapedWeather

import html5lib
class InPocasi(GenericParser):
    def parse(self) -> ScrapedWeather:
        page = requests.get("https://www.in-pocasi.cz/predpoved-pocasi/cz/moravskoslezsky/ostrava-295/")
        soup = bs4.BeautifulSoup(page.content,
                             'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
        print(soup.prettify())


if __name__ == "__main__":
    d = InPocasi()
    d.parse()