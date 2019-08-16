

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
        print("Warning! No agruments entered, reverting to defaults")
        start = 0
        end = 0

    return start, end

