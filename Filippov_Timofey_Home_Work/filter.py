from PIL import Image
import numpy as np


def Find_medS(array, i, j, size):
    """Определение средней освященности в группе пикселей

    >>>Find_medS(array, i, j, size)
    142

    """
    medS = 0
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            red = array[n][n1][0]
            green = array[n][n1][1]
            blue = array[n][n1][2]
            pixel = (int(red) + int(blue) + int(green)) / 3
            medS += pixel
    medS = int(medS // 100)
    return medS


def black_white(array, scale, height, input, size, width):
    """Присвоение заданному колличеству пикселей нужной градации серго"""
    for i in range(0, height - 1, size):
        for j in range(0, width - 1, size):
            medS = Find_medS(array, i, j, size)
            for n in range(i, i + size):
                for n1 in range(j, j + size):
                    array[n][n1][0] = int(medS // scale) * scale
                    array[n][n1][1] = int(medS // scale) * scale
                    array[n][n1][2] = int(medS // scale) * scale
    res = Image.fromarray(array)
    res.save(input[1])


print('Введите полное имя исходного изображения и результата. '
      'Размер мозайки. Градацию серого. (разделитель - " ")')
inp = input().split(' ')
img = Image.open(inp[0])
mosSize = int(inp[2])
grayscale = int(inp[3])
arr = np.array(img)
height = len(arr)
width = len(arr[1])
black_white(arr, grayscale, height, inp, mosSize, width)
