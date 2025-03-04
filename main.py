import cv2 as cv
import numpy as np

img_bruit = cv.imread('piecesbruit.png', cv.IMREAD_GRAYSCALE)

def recuperer_pixels_voisins(x, y, img):
    voisins = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if 0 <= nx < img.shape[0] and 0 <= ny < img.shape[1]:
                voisins.append(img[nx, ny])
    return voisins

def appliquer_filtre_median(img):
    img_filtre = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_filtre[i, j] = np.median(recuperer_pixels_voisins(i, j, img))
    return img_filtre

def appliquer_filtre_moyenne(img):
    img_filtre = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_filtre[i, j] = np.mean(recuperer_pixels_voisins(i, j, img))
    return img_filtre

w = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
w_sum = np.sum(w)


def ponderation(img, x, y):
    s = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if 0 <= nx < img.shape[0] and 0 <= ny < img.shape[1]:
                s += img[nx, ny] * w[i, j]

    return s / w_sum

def appliquer_filtre_moyenne_ponderee(img):
    img_filtre = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_filtre[i, j] = ponderation(img, i, j)
    return img_filtre

def main():
    img_filtre = appliquer_filtre_moyenne_ponderee(img_bruit)

    cv.imwrite('piecesfiltre_moyenne_ponderee.png', img_filtre)

if __name__ == '__main__':
    main()