from skimage.segmentation import slic
from collections import deque
from skimage import io
import numpy as np
import cv2

# SLIC da biblioteca


def SLIC(img):
    result_slic = slic(img, n_segments=256, sigma=5,
                       multichannel=True, start_label=1, convert2lab=True)
    result_slic = np.uint8(result_slic)

    return result_slic

# Função pega os vizinhos


def get_neighbors(rows, columns, pixel):
    return np.mgrid[
        max(0, pixel[0] - 1):min(rows, pixel[0] + 2),
        max(0, pixel[1] - 1):min(columns, pixel[1] + 2)
    ].reshape(2, -1).T

# Função watershed


def watershed(img):
    mask = -2
    wshd = 0
    init = -1
    inqe = -3
    level = 256
    current_label = 0
    flag = False
    fifo = deque()

    rows, columns = img.shape
    total = rows * columns
    result_watershed = np.full((rows, columns), init, np.int32)

    reshaped_image = img.reshape(total)

    pixels = np.mgrid[0:rows, 0:columns].reshape(2, -1).T

    neighbors = np.array([get_neighbors(rows, columns, p)
                         for p in pixels], dtype=object)
    if len(neighbors.shape) == 3:
        neighbors = neighbors.reshape(rows, columns, -1, 2)
    else:
        neighbors = neighbors.reshape(rows, columns)

    indices = np.argsort(reshaped_image)
    sorted_image = reshaped_image[indices]
    sorted_pixels = pixels[indices]

    level = np.linspace(sorted_image[0], sorted_image[-1], level)
    level_indices = []
    current_level = 0

    for i in range(total):
        if sorted_image[i] > level[current_level]:
            while sorted_image[i] > level[current_level]:
                current_level += 1
            level_indices.append(i)
    level_indices.append(total)

    start_index = 0
    for stop_index in level_indices:
        # mask all pixels at the current level.
        for p in sorted_pixels[start_index:stop_index]:
            result_watershed[p[0], p[1]] = mask

            for q in neighbors[p[0], p[1]]:
                if result_watershed[q[0], q[1]] >= wshd:
                    result_watershed[p[0], p[1]] = inqe
                    fifo.append(p)
                    break

        while fifo:
            p = fifo.popleft()
            for q in neighbors[p[0], p[1]]:
                lab_p = result_watershed[p[0], p[1]]
                lab_q = result_watershed[q[0], q[1]]
                if lab_q > 0:
                    if lab_p == inqe or (lab_p == wshd and flag):
                        result_watershed[p[0], p[1]] = lab_q
                    elif lab_p > 0 and lab_p != lab_q:
                        result_watershed[p[0], p[1]] = wshd
                        flag = False
                elif lab_q == wshd:
                    if lab_p == inqe:
                        result_watershed[p[0], p[1]] = wshd
                        flag = True
                elif lab_q == mask:
                    result_watershed[q[0], q[1]] = inqe
                    fifo.append(q)

        for p in sorted_pixels[start_index:stop_index]:

            if result_watershed[p[0], p[1]] == mask:
                current_label += 1
                fifo.append(p)
                result_watershed[p[0], p[1]] = current_label
                while fifo:
                    q = fifo.popleft()
                    for r in neighbors[q[0], q[1]]:
                        if result_watershed[r[0], r[1]] == mask:
                            fifo.append(r)
                            result_watershed[r[0], r[1]] = current_label

        start_index = stop_index

    result_watershed = np.uint8(result_watershed)

    return result_watershed


# recebe a imagem
filename1 = "img_a.png"
filename2 = "img_b.jpg"

# lê a imagem
img_a = cv2.imread(filename1, 0)
img_b = io.imread(filename2)
# chama a função
resultWatershed = watershed(img_a)
resultSLIC = SLIC(img_b)

cv2.imwrite("watershed.png", resultWatershed)
io.imsave("SLIC.jpg", resultSLIC)
