import numpy as np
import cv2


def otsu(img):
    t, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return otsu


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
result_otsu = otsu(img_a)

cv2.imwrite("otsu.png", result_otsu)
