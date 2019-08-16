

import sys
import csv


def save_csv(data, path):

    print("Writing data to [{}]... ".format(path), end="")

    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['url', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for item in data:
            writer.writerow(item)

    print("Done")


def process_args():

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except:
        print("Warning! No agruments entered, reverting to defaults")
        start = 0
        end = 0

    return start, end

