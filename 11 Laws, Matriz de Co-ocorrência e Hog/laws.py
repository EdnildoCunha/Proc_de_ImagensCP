import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import signal as sg


def normalize(convolve_image):
    return 255.*np.absolute(convolve_image)/np.max(convolve_image)


img = cv2.imread('img_a.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = np.copy(gray.astype(np.float64))
(rows, cols) = gray.shape[:2]

# Criando um espaço para receber as convoluções
conv_maps = np.zeros((rows, cols, 16), np.float64)

# Criando um array de vetores de filtro de Laws
filter_vectors = np.array([[1, 4, 6,  4, 1],
                           [-1, -2, 0, 2, 1],
                           [-1, 0, 2, 0, 1],
                           [1, -4, 6, -4, 1]])


filters = list()
for ii in range(4):
    for jj in range(4):
        filters.append(np.matmul(filter_vectors[ii][:].reshape(
            5, 1), filter_vectors[jj][:].reshape(1, 5)))

# Preprocessando a imagem
smooth_kernel = (1/25)*np.ones((5, 5))
gray_smooth = sg.convolve(gray2, smooth_kernel, "same")
gray_processed = np.abs(gray2 - gray_smooth)

# Convolucionando as matrizes de laws
for ii in range(len(filters)):
    conv_maps[:, :, ii] = sg.convolve(gray_processed, filters[ii], 'same')

# Criando o mapa de texturas
texture_map = normalize((conv_maps[:, :, 1]+conv_maps[:, :, 4])//2)


plt.figure('Resultado de Texturas')
plt.imshow(texture_map, 'gray')
plt.show()
