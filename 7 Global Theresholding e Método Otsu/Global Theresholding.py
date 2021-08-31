import numpy as np
import cv2


def intens_media(img):

    int_media = np.mean(img)

    return int_media


def Tfinder(img, Tvalue, delta_T=1.0):
    number_iteration = 0

    # Step-2: Divide the images in two parts

    G1 = []
    G2 = []

    rows = img.shape[0]
    cols = img.shape[1]
    for r in range(rows):
        for c in range(cols):
            if img[r, c] <= Tvalue:
                G1.append(img[r, c])
            elif img[r, c] > Tvalue:
                G2.append(img[r, c])

    # Step-3: Find the mean of two parts
    mean_low = np.mean(G1)
    mean_high = np.mean(G2)

    # Step-4: Calculate the new threshold
    new_thres = (mean_low + mean_high)/2

    # Step-5: Stopping criteria, otherwise iterate
    if abs(new_thres-Tvalue) < delta_T:
        return new_thres
    else:
        return Tfinder(img, Tvalue=new_thres, delta_T=1.0)


def global_theresholding(img):
    Tvalue = Tfinder(img, intens_media(img))
    # highest value
    val_high = 255
    # lower value
    val_low = 0

    rows = img.shape[0]
    cols = img.shape[1]

    result = np.zeros(rows*cols).reshape((rows, cols))
    # calculate global thresholding
    for r in range(rows):
        for c in range(cols):
            if img[r, c] > Tvalue:
                result[r, c] = val_high
            else:
                result[r, c] = val_low
    return result


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
result_globalThresholding = global_theresholding(img_a)

cv2.imwrite("globaltheres.png", result_globalThresholding)
