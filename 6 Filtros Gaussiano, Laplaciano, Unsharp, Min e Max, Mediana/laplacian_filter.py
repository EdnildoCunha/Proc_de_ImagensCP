import numpy as np
import cv2


laplace_operator = np.array(
    [[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]])
# Laplace


def laplacian_filter(img, operator):
    [rows, columns] = np.shape(img)
    result_laplace = np.zeros(shape=(rows, columns))

    for i in range(rows-2):
        for j in range(columns-2):
            result_laplace[i, j] = np.sum(
                np.multiply(operator, img[i:i+3, j:j+3]))

    return result_laplace


# nome do arquivo
filename = "img_a.png"
# le o arquivo
img_a = cv2.imread(filename, 0)
# chama a função
laplacian_filter = laplacian_filter(img_a, laplace_operator)
# escreve a função
cv2.imwrite("laplacian_filter.png", laplacian_filter)
