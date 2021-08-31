import numpy as np
import cv2

# Função rotacionar


def rotation(img, angle, scale):
    # Pega a imagem e o ângulo para realizar a rotação da imagem

    rows, cols = img.shape[:2]

    center_point = (rows/2, cols/2)  # ponto central da figura

    rotate = cv2.getRotationMatrix2D(center_point, angle, scale)

    img_rot = cv2.warpAffine(img, rotate, (rows, cols))

    return img_rot

# Função translação


def translation(img, x_shift, y_shift):

    rows, cols = img.shape[:2]

    translate = np.float32([[1, 0, x_shift], [0, 1, y_shift]])

    img_transl = cv2.warpAffine(img, translate, (rows, cols))

    return img_transl

# função espelhamento


def mirroring(img):

    img_mirror = cv2.flip(img, 1)

    return img_mirror

# função escalar


def scale(img, x_scale, y_scale):

    rows, cols = img.shape[:2]

    img_scale = cv2.resize(img, dsize=(x_scale * rows, y_scale * cols),
                           interpolation=cv2.INTER_CUBIC)

    return img_scale

# operação rigida


def rigida(img, angle_rig, scale_rig, x_shift_rig, y_shift_rig):

    img_rot = rotation(img, angle_rig, scale_rig)

    result_rigida = translation(img_rot, x_shift_rig, y_shift_rig)

    return result_rigida

# operação afim


def afim(img, angle, scale):

    img2 = mirroring(img)

    rows, cols = img2.shape[:2]

    srcTri = np.array([[0, 0], [rows - 1, 0],
                      [0, cols - 1]]).astype(np.float32)
    dstTri = np.array([[0, rows*0.33], [rows*0.85, cols
                      * 0.25], [rows*0.15, cols*0.7]]).astype(np.float32)

    warp_mat = cv2.getAffineTransform(srcTri, dstTri)

    warp_dst = cv2.warpAffine(img2, warp_mat, (rows, cols))

    rows2, cols2 = warp_dst.shape[:2]

    center_point2 = (rows/2, cols/2)

    rot_mat = cv2.getRotationMatrix2D(center_point2, angle, scale)

    result_afim = cv2.warpAffine(
        warp_dst, rot_mat, (rows2, cols2))

    return result_afim


# nome do arquivo
filename = "img_a.png"
# le o arquivo
img_a = cv2.imread(filename, 0)

# chama as funções

result_rot = rotation(img_a, 45, 1.0)
result_transl = translation(img_a, 20, -30)
result_scale = scale(img_a, 2, 3)
result_rigida = rigida(img_a, 45, 1.0, 10, 15)
result_afim = afim(img_a, 30, 0.6)

result_espelho = mirroring(img_a)

# salva os arquivos após as operações
cv2.imwrite("img_rot.png", result_rot)
cv2.imwrite("img_transl.png", result_transl)
cv2.imwrite("img_scale.png", result_scale)
cv2.imwrite("img_rigida.png", result_rigida)
cv2.imwrite("img_afim.png", result_afim)


cv2.imwrite("img_espelho.png", result_espelho)
