import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import rectangle, opening
from skimage.measure import label

def morfologia2():
    # Lee la imagen
    I = cv2.imread('lineas.jpg')
    
    # Convierte la imagen a escala de grises
    I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    
    # Binariza la imagen (umbral en 128)
    _, I_bin = cv2.threshold(I_gray, 128, 255, cv2.THRESH_BINARY)
    
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 3, 1)
    plt.imshow(I_bin, cmap='gray')
    plt.title('Imagen Binarizada')
    
    # Detectar líneas horizontales
    se_hor = np.ones((1, 16), dtype=np.uint8)  # elemento estructural (línea horizontal de longitud 16)
    J_hor = opening(I_bin // 255, se_hor)
    L_hor, n_hor = label(J_hor, return_num=True)
    plt.subplot(2, 3, 2)
    plt.imshow(J_hor, cmap='gray')
    plt.title(f'Horizontales: {n_hor}')
    
    # Detectar líneas verticales
    se_ver = np.ones((16, 1), dtype=np.uint8)  # elemento estructural (línea vertical de longitud 16)
    J_ver = opening(I_bin // 255, se_ver)
    L_ver, n_ver = label(J_ver, return_num=True)
    plt.subplot(2, 3, 3)
    plt.imshow(J_ver, cmap='gray')
    plt.title(f'Verticales: {n_ver}')
    
    # Detectar líneas diagonales (pendiente +)
    se_diag_pos = np.eye(20, dtype=np.uint8)  # elemento estructural diagonal (+45 grados)
    J_diag_pos = opening(I_bin // 255, se_diag_pos)
    L_diag_pos, n_diag_pos = label(J_diag_pos, return_num=True)
    plt.subplot(2, 3, 4)
    plt.imshow(J_diag_pos, cmap='gray')
    plt.title(f'Diagonales +: {n_diag_pos}')
    
    # Detectar líneas diagonales (pendiente -)
    se_diag_neg = np.fliplr(np.eye(20, dtype=np.uint8))  # elemento estructural diagonal (-45 grados)
    J_diag_neg = opening(I_bin // 255, se_diag_neg)
    L_diag_neg, n_diag_neg = label(J_diag_neg, return_num=True)
    plt.subplot(2, 3, 5)
    plt.imshow(J_diag_neg, cmap='gray')
    plt.title(f'Diagonales -: {n_diag_neg}')
    
    # Mostrar todas las subtramas
    plt.tight_layout()
    plt.show()

# Ejecutar la función
morfologia2()
