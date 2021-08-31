import numpy as np
import cv2

# Filtro Gaussiano


def Gauss_filter(img):
    rows, cols = img.shape[:2]

    result_gaussfilter = np.zeros((rows, cols), dtype=np.float32)

    for r in range(rows):
        for c in range(cols):

            # Filtro Laplaciano
            # Filtro Unsharp
            # Filtro MIN e MAX
            # Filtro Mediano


            # nome do arquivo
filename = "img_a.png"
# le o arquivo
img_a = cv2.imread(filename, 0)
