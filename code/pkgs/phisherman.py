

import os
import multiprocessing as mp
import requests
from bs4 import BeautifulSoup as bs


class Phisherman:

    def __init__(self, start, end, mp=True):
        self.__start = start
        self.__end = end
        self.__njobs = self.__set_njobs(mp)

    
    def __get_start(self):
        return self.__start

    
    def __set_start(self, start):
        self.__start = start


    def __get_end(self):
        return self.__end


    def __set_end(self, end):
        self.__end = end


    def __get_njobs(self):
        return self.__njobs


    def __set_njobs(self, mp):
        if mp:
            self.__njobs = os.cpu_count() - 1
        else:
            self.__njobs = 1


    def __make_page_url(self, page):
        return "https://www.phishtank.com/phish_search.php?page={}\
            &active=y&valid=y&Search=Search".format(page)


    def __make_detail_page_url(self, id):
        return "https://www.phishtank.com/phish_detail.php?\
            phish_id={}".format(id)


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


    start = property(__get_start, __set_start)
    end = property(__get_end, __set_end)
    njobs = property(__get_njobs, __set_njobs)

