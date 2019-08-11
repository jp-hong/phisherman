

import requests
from bs4 import BeautifulSoup as bs


def make_page_url(page):
    return "https://www.phishtank.com/phish_search.php?page={}\
        &active=y&valid=y&Search=Search".format(page)


def make_detail_page_url(id):
    return "https://www.phishtank.com/phish_detail.php?phish_id={}".format(id)


def get_ids(page):
    response = requests.get(make_page_url(page))
    soup = bs(response.content, "html.parser")
    elements = soup.select(".value:first-child > a")
    ids = [element.text for element in elements]
    return ids


def get_data(id):
    response = requests.get(make_detail_page_url(id))
    soup = bs(response.content, "html.parser")
    phish_url = soup.select_one(".padded > div:nth-child(4) > \
        span:nth-child(1) > b:nth-child(1)").text
    return phish_url


def test():
    ids = get_ids(0)
    print(ids)


test()

