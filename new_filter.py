from PIL import Image
import numpy as np


def pixel_art_filter(mosaic_side, step):
    """
    Start of image filtering
    :param mosaic_side: int
    :param step: int
    """
    img_length, img_height = len(img_arr), len(img_arr[1])
    segment_x, segment_y = np.arange(0, img_length, mosaic_side), np.arange(0, img_height, mosaic_side)
    [[pixel_coloring(x, y, mosaic_side, step) for y in segment_y] for x in segment_x]


def find_average_brightness(x, y, mosaic_side):
    """
    Returns the average brightness in the processed area of the image
    :param x: int
    :param y: int
    :param mosaic_side: int
    :return: int
    >>> find_average_brightness(2, 2, 10)
    175
    >>> find_average_brightness(4, 4, 16)
    166
    >>> find_average_brightness(10, 10, 30)
    184
    >>> find_average_brightness(0, 0, 0)
    Traceback (most recent call last):
    ZeroDivisionError: integer division or modulo by zero
    >>> find_average_brightness(-1, -1, 5)
    0
    >>> find_average_brightness(0, 0, 5)
    176
    >>> find_average_brightness('a', 'b', 0)
    Traceback (most recent call last):
    TypeError: can only concatenate str (not "int") to str
    """
    result = np.sum(img_arr[x: x + mosaic_side, y: y + mosaic_side] / 3)
    return int(result) // mosaic_side ** 2


def pixel_coloring(x, y, mosaic_side, step):
    """
    Fills pixels in the square area of the image with a new color
    :param x: int
    :param y: int
    :param mosaic_side: int
    :param step: int
    """
    avg_brightness = find_average_brightness(x, y, mosaic_side)
    img_arr[x:x + mosaic_side, y:y + mosaic_side][:] = int(avg_brightness // step) * step


def main():
    np.seterr(over='ignore')
    global img_arr
    original_img_name = input("Введите имя исходного изображения: ")
    filtered_img_name = input("Введите имя конечного изображения: ")
    mosaic_side, step = map(int, input("Задайте значения размера мозайки и шага яркости через пробел: ").split())
    print("Обработка изображения началась, ожидайте")
    img_arr = np.array(Image.open(original_img_name))
    pixel_art_filter(mosaic_side, 255 // step)
    changed_img = Image.fromarray(img_arr)
    changed_img.save(filtered_img_name)
    print("Обработка успешно завершена")


if __name__ == '__main__':
    main()