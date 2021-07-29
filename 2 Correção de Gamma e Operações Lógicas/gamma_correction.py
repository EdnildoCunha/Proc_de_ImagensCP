import cv2


def gamma(img, gamma):
  # funcao para correcao gamma
    correction_gamma = (img) ** (gamma)
    return correction_gamma


# lendo o arquivo
filename = "img1_gs.jpg"


img = cv2.imread(filename, 0)
# resultado para valor de gama menor que 1
resultado1 = gamma(img, 0.8)
# resultado para valor de gama maior que 1
resultado2 = gamma(img, 1.5)

# salvando as imagens
cv2.imwrite("img1_gammamenorque1.jpg", resultado1)
cv2.imwrite("img1_gammamaiorque1.jpg", resultado2)
