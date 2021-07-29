import cv2
import numpy as np
from skimage import exposure


# stretching


def stretching(img):
    rows, cols = img.shape[:2]

    result_str = np.zeros((rows, cols), dtype=np.float32)

    min_value = np.min(img)
    max_value = np.max(img)

    for r in range(rows):
        for c in range(cols):
            result_str[r, c] = np.ceil(
                (255 * (img[r, c] - min_value)) / (max_value - min_value))

    return np.uint8(result_str)


# linear mapping


def linear_map(img, a, b):
    # a = coef angular, b= intecepta a no eixo da escala de cinza
    rows, cols = img.shape[:2]

    result_lin_map = np.zeros((rows, cols), dtype=np.float32)

    for r in range(rows):
        for c in range(cols):
            if a*img[r, c]+b > 255:
                result_lin_map[r, c] = 255
            else:
                result_lin_map[r, c] = a*img[r, c]+b

    return np.uint8(result_lin_map)


# equalização


def equalize(img):
    rows, cols = img.shape[:2]
    histogram = np.zeros(256)
    acumulateHistogram = np.zeros(256, dtype=np.float32)

    factor = 255 / (rows * cols)

    result_eq = np.zeros((rows, cols), dtype=np.float32)

    for r in range(rows):
        for c in range(cols):
            value = img[r, c]

            histogram[value] += 1

    acumulateHistogram = np.array(histogram)

    for i in range(256):
        if i == 0:
            acumulateHistogram[i] = histogram[i]
        else:
            acumulateHistogram[i] += acumulateHistogram[i - 1]

    for i in range(256):
        aux = acumulateHistogram[i] * factor

        acumulateHistogram[i] = round(aux)

    for r in range(rows):
        for c in range(cols):
            value = img[r, c]

            value = acumulateHistogram[value]

            result_eq[r, c] = value

    return np.uint8(result_eq)


# especificação de histograma


def histogram_matching(img, ref):

    matched = exposure.match_histograms(img, ref)

    return matched


# Nomes dos arquivos


filename = "img_a.jpg"

ref_filename = "img_ref.png"


# Le os arquivos


img_a = cv2.imread(filename, 0)

img_ref = cv2.imread(ref_filename, 0)


# chama as funções


result_stretching = stretching(img_a)

# linear mapping y = 4*x + 5  (a*x + b)
result_linear_mapping = linear_map(img_a, 4, 5)

result_equalizing = equalize(img_a)

result_matching = histogram_matching(img_a, img_ref)


# Salva as imagens apos as operações


cv2.imwrite("img_stretching.jpg", result_stretching)

cv2.imwrite("img_lin_map.jpg", result_linear_mapping)

cv2.imwrite("img_equalization.jpg", result_equalizing)

cv2.imwrite("img_matching.jpg", result_matching)
