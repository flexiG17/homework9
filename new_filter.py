from PIL import Image
import numpy as np


def pixel_art_filter(mosaic_side, step):
    img_length, img_height = len(img_arr), len(img_arr[1])
    segment_x, segment_y = np.arange(0, img_length, mosaic_side), np.arange(0, img_height, mosaic_side)
    [[pixel_coloring(x, y, mosaic_side, step) for y in segment_y] for x in segment_x]


def find_average_brightness(x, y, mosaic_side):
    result = np.sum(img_arr[x: x + mosaic_side, y: y + mosaic_side] / 3)
    return int(result) // mosaic_side ** 2


def pixel_coloring(x, y, mosaic_side, step):
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