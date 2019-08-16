

from pkgs.phisherman import Phisherman
from pkgs.util import *
import sys
import pickle


def crawl():
    pass


# test function
def test():
    start, end = process_args()
    phisherman = Phisherman(start, end)
    data = phisherman.crawl()

    print(len(data))

    for line in data:
        print(line)


test()