from threading import RLock
from common import get_pixel

lock = RLock()


def convert_grayscale(image, i, j, pixels):
    lock.acquire()
    pixel = get_pixel(image, i, j)

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
    print(str(i) + ' ' + str(j))
    pixels[i, j] = (int(gray), int(gray), int(gray))
    lock.release()