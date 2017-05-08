from PIL import Image


def open_image(path):
    new_image = Image.open(path)
    return new_image


def save_image(image, path):
    image.save(path, 'png')


def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image


def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    pixel = image.getpixel((i, j))
    return pixel
