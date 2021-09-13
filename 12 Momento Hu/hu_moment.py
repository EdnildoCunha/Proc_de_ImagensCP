import cv2
import numpy as np

# Hu moments


def Humoment(img):
    img = np.uint8(img)
    result_img = cv2.HuMoments(cv2.moments(img)).flatten()
    return print(result_img)


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
humoment = Humoment(img_a)
