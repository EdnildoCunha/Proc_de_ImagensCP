import numpy as np
import cv2
import math

# Operador Logarítmico


def log(imgA):

    # Recebe a quantidade de linhas
    rows = imgA.shape[0]
    # Recebe a quantidade de colunas
    cols = imgA.shape[1]

    # Define uma matriz resultado que receberá os valores com o mesmo número de linhas e colunas das imagens
    # de entrada
    result = np.zeros(rows*cols).reshape((rows, cols))

    # Calcula o valor da constante para o valor máximo + 1
    const = 255/(math.log(256))

    for r in range(rows):
        for c in range(cols):
            # Percorre as linhas e colunas e realiza a operação logarítmica
            result[r, c] = const*math.log(1+imgA[r, c])
    # retorna a matriz resultante
    return result


# recebe a imagem
filename1 = "img_a.png"
# lê as imagens
img_a = cv2.imread(filename1, 0)
# Chama a função
result_log = log(img_a)
# Salva a imagem resultante
cv2.imwrite("imgLog.png", result_log)
