import cv2
import numpy as np


def min(img, filter_size):
    value = 0
    edge = filter_size // 2

    rows, cols = img.shape

    result = np.ones((rows, cols), dtype=np.float32)

    for i in range(rows - edge):
        for j in range(cols - edge):

            for x in range(filter_size):
                for y in range(filter_size):
                    value += img[i - edge + x, j - edge + y]

            result[i, j] = np.round((value * 1) / (filter_size * filter_size))
            value = 0

    return np.uint8(result)


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
min_filter = min(img_a, 3)

cv2.imwrite("globaltheres.png", min_filter)
