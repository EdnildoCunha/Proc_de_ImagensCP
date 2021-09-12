import cv2
import numpy as np
from collections import defaultdict


def hough_circles(img, r_min, r_max, delta_r, num_theta):
    edge_img = cv2.Canny(img, 100, 200)

    rows, columns = edge_img.shape[:2]

    dtheta = int(360 / num_theta)

    theta = np.arange(0, 360, step=dtheta)

    radius_range = np.arange(r_min, r_max, step=delta_r)

    cos_theta = np.cos(np.deg2rad(theta))
    sin_theta = np.sin(np.deg2rad(theta))

    circle_candidates = []
    for r in radius_range:
        for t in range(num_theta):
            circle_candidates.append(
                (r, int(r * cos_theta[t]), int(r * sin_theta[t])))
    accumulator = defaultdict(int)

    for y in range(rows):
        for x in range(columns):
            if edge_img[y][x] != 0:
                for r, rcos_t, radius_rangein_t in circle_candidates:
                    x_center = x - rcos_t
                    y_center = y - radius_rangein_t
                    accumulator[(x_center, y_center, r)] += 1

    # Output img with detected lines drawn
    output_img = img.copy()
    # Output list of detected circles. A single circle would be a tuple of (x,y,r,threshold)
    out_circles = []

    for candidate_circle, votes in sorted(accumulator.items(), key=lambda i: -i[1]):
        x, y, r = candidate_circle
        current_vote_percentage = votes / num_theta
        if current_vote_percentage >= 0.4:
            out_circles.append((x, y, r, current_vote_percentage))
            print(x, y, r, current_vote_percentage)

    # Desenha circulos na img de saida
    for x, y, r, v in out_circles:
        output_img = cv2.circle(output_img, (x, y), r, (0, 255, 0), 2)

    output_img = np.uint8(output_img)

    return output_img


# recebe a imagem
filename = "img_a.png"

# lê a imagem
img_a = cv2.imread(filename, 0)

# chama a função
houghCircles = hough_circles(img_a, 10, 200, 1, 100)

cv2.imwrite("hough_circles.png", hough_circles)
