

from pkgs.phisherman import Phisherman
from pkgs.util import process_args, save_csv


def crawl():
    pass


# test function
def test():
    start, end = process_args()
    phisherman = Phisherman(start, end)
    data = phisherman.crawl()
    save_csv(data, "data.csv")
    

test()