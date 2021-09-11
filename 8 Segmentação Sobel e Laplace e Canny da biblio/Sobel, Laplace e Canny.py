import numpy as np
import cv2
from numpy.random.mtrand import laplace

sobel_operator = np.array(
    [[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]])

# Função de detecção de bordas por sobel


def Sobel(img, operator):
    [rows, columns] = np.shape(img)
    result_sobel = np.zeros(shape=(rows, columns))
    for i in range(rows - 2):
        for j in range(columns - 2):
            image_x = np.sum(np.multiply(operator, img[i:i + 3, j:j + 3]))
            # transposta do operador
            image_y = np.sum(np.multiply(
                np.flip(operator.T, axis=0), img[i:i + 3, j:j + 3]))
            result_sobel[i + 1, j + 1] = np.sqrt(image_x ** 2 + image_y ** 2)
    return result_sobel


laplace_operator = np.array(
    [[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]])
# Laplace


def Laplace(img, operator):
    [rows, columns] = np.shape(img)
    result_laplace = np.zeros(shape=(rows, columns))

    for i in range(rows-2):
        for j in range(columns-2):
            result_laplace[i, j] = np.sum(
                np.multiply(operator, img[i:i+3, j:j+3]))

    return result_laplace


def Canny(img):
    result_canny = cv2.Canny(img, 20, 120)
    return result_canny


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
result_sobel = Sobel(img_a, sobel_operator)
result_laplace = Laplace(img_a, laplace_operator)
result_canny = Canny(img_a)

cv2.imwrite("sobel.png", result_sobel)
cv2.imwrite("laplace.png", result_laplace)
cv2.imwrite("canny.png", result_canny)
