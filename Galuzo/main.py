from threading import Thread, active_count
import sys
from median import convert_median
import common
import time
import os
from grayscale import convert_grayscale


def main(argv):
    original = common.open_image(argv[2])

    width, height = original.size

    new = common.create_image(width, height)
    pixels = new.load()
    worker = None

    print(argv)

    if argv[1].lower() == 'grayscale':
        worker = convert_grayscale
    elif argv[1].lower() == 'median':
        worker = convert_median

    start_time = time.time()
    for i in range(width):
        for j in range(height):
            thread = Thread(target=worker, args=(original, i, j, pixels))
            thread.start()

    while active_count() > 1:
        continue
    end_time = time.time() - start_time
    file_size = os.stat(argv[2]).st_size
    print('Mb/sec ' + str(file_size / end_time))
    print('Pixels/sec ' + str(width * height / end_time))
    common.save_image(new, argv[3])


if __name__ == "__main__":
    try:
        main(sys.argv)
    except IndexError:
        print('IndexError exception. Invalid argv count')
