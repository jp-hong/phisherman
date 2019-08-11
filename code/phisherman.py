

import requests
from bs4 import BeautifulSoup as bs


def make_page_url(page):
    return "https://www.phishtank.com/phish_search.php?page={}\
        &active=y&valid=y&Search=Search".format(page)


def make_detail_page_url(id):
    return "https://www.phishtank.com/phish_detail.php?phish_id={}".format(id)


def get_data(id):
    response = requests.get(make_detail_page_url(id))
    soup = bs(response.content, "html.parser")
    phish_url = soup.select_one(".padded > div:nth-child(4) > \
        span:nth-child(1) > b:nth-child(1)").text
    return phish_url


def test():
    url = get_data(6154916)
    print(url)


test()

