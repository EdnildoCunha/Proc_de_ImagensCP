import numpy as np
import cv2


def median_filter(img, filter_size):
    temp = []
    indexer = filter_size // 2

    rows = img.shape[0]
    cols = img.shape[1]

    result = np.zeros(rows*cols).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
            for f in range(filter_size):
                if r + f - indexer < 0 or r + f - indexer > rows - 1:
                    for m in range(filter_size):
                        temp.append(0)
                else:
                    if c + f - indexer < 0 or c + indexer > cols - 1:
                        temp.append(0)
                    else:
                        for n in range(filter_size):
                            temp.append(img[r + f - indexer][c + f - indexer])

            temp.sort()
            result[r][c] = temp[len(temp) // 2]
            temp = []
    return result


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
mediana = median_filter(img_a, 3)

cv2.imwrite("median_filter.png", mediana)
