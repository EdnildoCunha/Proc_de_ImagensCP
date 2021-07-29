import numpy as np
import cv2


def quantize(img, k):
    img_quantize = np.float32(img)
    rate = 256/k
    quantized = (img_quantize/rate)
    return np.uint8(quantized)*rate


filename = "img1_gs.jpg"


img = cv2.imread(filename, 0)
resultado2 = quantize(img, 8)
cv2.imwrite("img1_quantized.jpg", resultado2)
