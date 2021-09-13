from skimage.io import imread
from skimage.feature import hog
import cv2


def HOG(img):
    fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True, multichannel=True)
    print(fd)
    print(hog_image)

    return hog_image


filename = "img_b.jpg"

# lê a imagem
img_b = imread(filename, 0)

# chama a função
result_hog = HOG(img_b)

cv2.imwrite("hog.jpg", result_hog)
