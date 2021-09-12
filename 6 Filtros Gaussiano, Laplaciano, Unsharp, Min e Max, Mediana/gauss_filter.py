import numpy as np
import cv2


def gauss_filter(img):

    value = 0
    mask = np.array([1, 2, 1, 2, 4, 2, 1, 2, 1])

    windowsize = 3
    edge = windowsize // 2

    neighbors = []

    rows = img.shape[0]
    cols = img.shape[1]

    result = np.ones((rows, cols), dtype=np.float32)

    for i in range(edge, rows - edge):
        for j in range(edge, cols - edge):
            for x in range(windowsize):
                for y in range(windowsize):
                    neighbors.append(img[i-edge+x, j-edge+y])

            for k in range(len(neighbors)):
                value += neighbors[k] * mask[k]

            value = np.round(value / 16)

            if value < 0:
                value = 0
            if value > 255:
                value = 255

            result[i, j] = value
            value = 0
            neighbors.clear()

    return np.uint8(result)


    # recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
gauss = gauss_filter(img_a)

cv2.imwrite("gauss_filter.png", gauss)
