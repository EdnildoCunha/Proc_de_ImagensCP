import numpy as np
from operator import xor
import cv2

# Funcao AND


def logic_and(imgA, imgB):
    # Pega a quantidade de linhas
    rows = imgA.shape[0]
    # Pega a quantidade de colunas
    cols = imgA.shape[1]

    # Cria uma matriz de zeros com o tamanho das imagens operadas
    result = np.zeros(rows*cols).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
          # compara em cada linha e coluna o valor naquele local e realiza  a operacao and
            if imgA[r, c] == 255 and imgB[r, c] == 255:
              # se for true o resultado recebe naquela posicao o valor 255
                result[r, c] = 255
    return result

# Funcao OR


def logic_or(imgA, imgB):
   # Pega a quantidade de linhas
    rows = imgA.shape[0]
    # Pega a quantidade de colunas
    cols = imgA.shape[1]

    # Cria uma matriz de zeros com o tamanho das imagens operadas
    result = np.zeros(rows*cols,  dtype=np.uint32).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
          # compara em cada linha e coluna o valor naquele local e realiza  a operacao or
            if imgA[r, c] == 255 or imgB[r, c] == 255:
              # se for true o resultado recebe naquela posicao o valor 255
                result[r, c] = 255
    return result

# Funcao XOR


def logic_xor(imgA, imgB):
   # Pega a quantidade de linhas
    rows = imgA.shape[0]
    # Pega a quantidade de colunas
    cols = imgA.shape[1]

    # Cria uma matriz de zeros com o tamanho das imagens operadas
    result = np.zeros(rows*cols).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
          # compara em cada linha e coluna o valor naquele local e realiza  a operacao xor
            if xor(imgA[r, c], imgB[r, c]) == 255:
              # se for true o resultado recebe naquela posicao o valor 255
                result[r, c] = 255
    return result

# Funcao Not


def logic_not(imgA):
   # Pega a quantidade de linhas
    rows = imgA.shape[0]
    # Pega a quantidade de colunas
    cols = imgA.shape[1]

    # Cria uma matriz de zeros com o tamanho das imagens operadas
    result = np.zeros(rows*cols).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
          # compara em cada linha e coluna o valor naquele local e realiza  a operacao not que inverte as cores da imagem
            if imgA[r, c] == 255:
              # se for true o resultado recebe naquela posicao o valor 0
                result[r, c] = 0
            else:
              # caso contrario recebe 255
                result[r, c] = 255
    return result


filename1 = "img_a.png"
filename2 = "img_b.png"

img_a = cv2.imread(filename1, 0)
img_b = cv2.imread(filename2, 0)

resultado_and = logic_and(img_a, img_b)
resultado_or = logic_or(img_a, img_b)
resultado_xor = logic_xor(img_a, img_b)
resultado_not = logic_not(img_a)

cv2.imwrite("imgAnd.png", resultado_and)
cv2.imwrite("imgOr.png", resultado_or)
cv2.imwrite("imgXor.png", resultado_xor)
cv2.imwrite("imgNot.png", resultado_not)
