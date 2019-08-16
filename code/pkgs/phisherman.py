

from os import cpu_count
import multiprocessing as mp
import threading as th
import requests
from bs4 import BeautifulSoup as bs


class Phisherman:

    def __init__(self, start, end, use_mp=True):
        self.__start = start
        self.__end = end
        self.__njobs = self.__set_njobs(use_mp)

    
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


    def __set_njobs(self, use_mp):
        if use_mp:
            return cpu_count() - 1
        else:
            return 1


    def __make_page_url(self, page):
        return "https://www.phishtank.com/phish_search.php?page={}\
            &active=y&valid=y&Search=Search".format(page)


    def __make_detail_page_url(self, url_id):
        return "https://www.phishtank.com/phish_detail.php?\
            phish_id={}".format(url_id)


    def __get_ids(self, page):
        response = requests.get(self.__make_page_url(page))
        soup = bs(response.content, "html.parser")
        elements = soup.select(".value:first-child > a")
        url_ids = [element.text for element in elements]
        return url_ids


    def __get_data(self, url_id):
        response = requests.get(self.__make_detail_page_url(url_id))
        soup = bs(response.content, "html.parser")

        phish_url = soup.select_one(".padded > div:nth-child(4) > \
            span:nth-child(1) > b:nth-child(1)").text

        date = self.__parse_date_string(soup.select_one(".small").text)
        return {"url": phish_url, "date": date}


    def __get_data_thread(self, url_id, page_data, th_lock):
        data = self.__get_data(url_id)

        th_lock.acquire()

        try:
            page_data.append(data)
        finally:
            th_lock.release()


    def __parse_date_string(self, date_str):
        return " ".join(date_str.split()[1:6])


    def __crawl(self):
        url_ids = []
        data = []
        
        for page in range(self.start, self.end + 1):
            url_ids += self.__get_ids(page)

        for url_id in url_ids:
            data.append(self.__get_data(url_id))

        return data


    def run(self):
        pass

        
    def test_run(self):
        return self.__crawl()


    start = property(__get_start, __set_start)
    end = property(__get_end, __set_end)
    njobs = property(__get_njobs)
