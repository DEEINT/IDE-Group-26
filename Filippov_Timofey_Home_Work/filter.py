from PIL import Image
import numpy as np

def Find_medS(arr, i, j, mosSize):
    """Определение средней освященности в группе пикселей

    >>>Find_medS(arr, i, j, mosSize)
    142

    """
    medS = 0
    for n in range(i, i + mosSize):
        for n1 in range(j, j + mosSize):
            red = arr[n][n1][0]
            green = arr[n][n1][1]
            blue = arr[n][n1][2]
            pixel = (int(red) + int(blue) + int(green))/3
            medS += pixel
    medS = int(medS // 100)
    return medS

def black_white(arr, grayscale, height, inp, mosSize, width):
    """Присвоение заданному колличеству пикселей нужной градации серго"""
    for i in range(0, height - 1, mosSize):
        for j in range(0, width - 1, mosSize):
            medS = Find_medS(arr, i, j, mosSize)
            for n in range(i, i + mosSize):
                for n1 in range(j, j + mosSize):
                    arr[n][n1][0] = int(medS // grayscale) * grayscale
                    arr[n][n1][1] = int(medS // grayscale) * grayscale
                    arr[n][n1][2] = int(medS // grayscale) * grayscale
    res = Image.fromarray(arr)
    res.save(inp[1])

print('Введите полное имя исходного изображения и результата.',
      'Размер мозайки. Градацию серого. (разделитель - " ")')
inp = input().split(' ')
img = Image.open(inp[0])
mosSize = int(inp[2])
grayscale = int(inp[3])
arr = np.array(img)
height = len(arr)
width = len(arr[1])
black_white(arr, grayscale, height, inp, mosSize, width)
