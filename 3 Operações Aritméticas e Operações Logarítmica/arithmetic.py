import numpy as np
import cv2
import math

# Operador de Adição de imagens~


def addition(imgA, imgB):

    # Ao transformar em matriz o numpy converte a matriz para um formato unsigned int 8 bits(valor máximo 255)
    # Para realizar contas que ultrapassem esses valores com essas matriz é necessário converter para um tipo
    # que suporte mais valores. O código a baixo converte para um tipo de unsigned int 16 bits.
    # Evitando o overflow.
    imgA = np.uint16(imgA)
    imgB = np.uint16(imgB)

    # Recebe a quantidade de linhas
    rows = imgA.shape[0]
    # Recebe a quantidade de colunas
    cols = imgA.shape[1]

    # Define uma matriz resultado que receberá os valores com o mesmo número de linhas e colunas das imagens
    # de entrada
    result = np.zeros(rows*cols, dtype=np.uint16).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
            # Percorre as linhas e colunas e realiza a soma dos valores ponto a ponto, caso a soma dê acima de
            # 255 isso é tratado atribuindo o valor máximo à matriz resultante
            if imgA[r, c]+imgB[r, c] > 255:
                result[r, c] = 255
            else:
                # Caso contrário é realizado a soma
                result[r, c] = imgA[r, c]+imgB[r, c]
    # Converte-se a matriz resultante para o tipo unsigned int 8 bits
    result = np.uint8(result)
    # retorna a matriz resultante
    return result

# Operador de Subtração de imagens


def subtraction(imgA, imgB):

    # Ao transformar em matriz o numpy converte a matriz para um formato unsigned int 8 bits(valor máximo 255)
    # Para realizar contas que recebam valores menores que zero com essas matriz é necessário converter para um tipo
    # que suporte mais valores. O código abaixo converte para um tipo de int 16 bits.
    # Evitando o overflow.
    imgA = np.int16(imgA)
    imgB = np.int16(imgB)

    # Recebe a quantidade de linhas
    rows = imgA.shape[0]
    # Recebe a quantidade de colunas
    cols = imgA.shape[1]

    # Define uma matriz resultado que receberá os valores com o mesmo número de linhas e colunas das imagens
    # de entrada
    result = np.zeros(rows*cols, dtype=np.int16).reshape((rows, cols))

    for r in range(rows):
        for c in range(cols):
            # Percorre as linhas e colunas e realiza a subtração dos valores ponto a ponto, caso a soma dê abaixo de
            # 0 isso é tratado atribuindo o valor mínimo à matriz resultante
            if imgA[r, c] - imgB[r, c] < 0:
                result[r, c] = 0
            else:
                # Caso contrário é realizado a subtração
                result[r, c] = imgA[r, c] - imgB[r, c]
    # Converte-se a matriz resultante para o tipo unsigned int 8 bits
    result = np.uint8(result)
    # retorna a matriz resultante
    return result

# Operador de Multiplicação de uma imagem por um fator


def multiplication(imgA, factor):
    # Recebe a quantidade de linhas
    rows = imgA.shape[0]
    # Recebe a quantidade de colunas
    cols = imgA.shape[1]
    # Define uma matriz resultado que receberá os valores com o mesmo número de linhas e colunas das imagens
    # de entrada
    result = np.zeros(rows*cols).reshape((rows, cols))
    for r in range(rows):
        for c in range(cols):
            # Percorre as linhas e colunas e realiza a multiplicção dos valores da matriz pelo fator
            result[r, c] = imgA[r, c] * factor
    # retorna a matriz resultante
    return result

# Operador de Divisão de uma imagem por um fator


def division(imgA, factor):
    # Recebe a quantidade de linhas
    rows = imgA.shape[0]
    # Recebe a quantidade de colunas
    cols = imgA.shape[1]
    # Define uma matriz resultado que receberá os valores com o mesmo número de linhas e colunas das imagens
    # de entrada
    result = np.zeros(rows*cols).reshape((rows, cols))
    for r in range(rows):
        for c in range(cols):
            # Percorre as linhas e colunas e realiza a divisão dos valores da matriz pelo fator
            result[r, c] = imgA[r, c] / factor
    # retorna a matriz resultante
    return result


# recebe as imagens
filename1 = "img_a.png"
filename2 = "img_b.png"

# lê as imagens
img_a = cv2.imread(filename1, 0)
img_b = cv2.imread(filename2, 0)

# Chama as funções
result_add = addition(img_a, img_b)
result_sub = subtraction(img_a, img_b)
result_mult = multiplication(img_b, 0.6)
result_div = division(img_b, 0.6)
# Salva as imagens resultantes
cv2.imwrite("imgAdd.png", result_add)
cv2.imwrite("imgSub.png", result_sub)
cv2.imwrite("imgMult.png", result_mult)
cv2.imwrite("imgDiv.png", result_div)
