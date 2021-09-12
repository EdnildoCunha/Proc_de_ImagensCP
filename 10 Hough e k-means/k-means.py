import cv2
import numpy as np

# Função k-means


def Kmeans(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixel_values = img.reshape((-1, 3))

    pixel_values = np.float32(pixel_values)
    # criterio de parada
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    # numero de clusters
    k = 3
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)

    labels = labels.flatten()

    segmented_img = centers[labels.flatten()]

    segmented_img = segmented_img.reshape(img.shape)

    return segmented_img


# recebe a imagem
img_b = cv2.imread("img_b.png")
# chama a função
k_means = Kmeans(img_b)
# Salva a imagem
cv2.imwrite("k_means.png", k_means)
