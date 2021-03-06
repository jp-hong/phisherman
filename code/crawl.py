

from pkgs.phisherman import Phisherman
import sys
import pickle


def save_pkl(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)


def save_csv(data, path):
    pass


def process_args():

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except:
        print("Warning! No agruments entered. Default start and end pages will be used.")
        start = 0
        end = 9

    try:
        if sys.argv[3] == "-mpdisable":
            mp = False
            print("Warning! Multiprocessing disabled")
    except:
        mp = True

    return start, end, mp


def crawl():
    
    start, end, mp = process_args()

    print("Crawling pages {} to {}, multiprocessing={}".format(start, end, mp))


# test function
def test():
    p = Phisherman(0, 1)
<<<<<<< HEAD
    phish_url, date = p.test_run()
    print(phish_url, date)
=======
    print(p.test_run())
>>>>>>> dev


test()
# crawl()