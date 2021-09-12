import cv2
import numpy as np


def unsharp_filter(img, k):
    fsmooth = cv2.GaussianBlur(img, (3, 3), 0)

    fsmooth = np.uint8(fsmooth)

    rows = img.shape[0]
    cols = img.shape[1]

    g = np.zeros((rows*cols), dtype=np.float32).reshape((rows, cols))
    result = np.zeros((rows*cols), dtype=np.float32).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
            if img[r, c] - fsmooth[r, c] > 255:
                g[r, c] = 255
            elif img[r, c] - fsmooth[r, c] < 0:
                g[r, c] = 0
            else:
                g[r, c] = img[r, c] - fsmooth[r, c]

    for r in range(rows):
        for c in range(cols):
            if img[r, c] - k*g[r, c] > 255:
                result[r, c] = 255
            elif img[r, c] - k*g[r, c] < 0:
                result[r, c] = 0
            else:
                result[r, c] = img[r, c] - k*g[r, c]

    result = np.uint8(result)

    return result


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
unsharp = unsharp_filter(img_a, 0.3)

cv2.imwrite("unsharp_filter.png", unsharp)
