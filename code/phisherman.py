

import requests
from bs4 import BeautifulSoup as bs


class Phisherman:

    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    
    def get_start(self):
        return self.__start

    
    def set_start(self, start):
        self.__start = start


    def get_end(self):
        return self.__end


    def set_end(self, end):
        self.__end = end


    def __make_page_url(self, page):
        return "https://www.phishtank.com/phish_search.php?page={}\
            &active=y&valid=y&Search=Search".format(page)


    def __make_detail_page_url(self, id):
        return "https://www.phishtank.com/phish_detail.php?phish_id={}".format(id)


    def __get_ids(self, page):
        response = requests.get(self.__make_page_url(page))
        soup = bs(response.content, "html.parser")
        elements = soup.select(".value:first-child > a")
        ids = [element.text for element in elements]
        return ids


    def __get_data(self, id):
        response = requests.get(self.__make_detail_page_url(id))
        soup = bs(response.content, "html.parser")
        phish_url = soup.select_one(".padded > div:nth-child(4) > \
            span:nth-child(1) > b:nth-child(1)").text
        return phish_url


    start = property(get_start, set_start)
    end = property(get_end, set_end)

