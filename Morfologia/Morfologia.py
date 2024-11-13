import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk, opening
from skimage.measure import label

def morfologia1():
    # Lee la imagen
    I = cv2.imread('puntos_lineas.jpg')
    
    # Convierte la imagen a escala de grises
    I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    
    # Binariza la imagen (umbral en 128)
    _, I_bin = cv2.threshold(I_gray, 128, 255, cv2.THRESH_BINARY)
    
    # Muestra la imagen binarizada
    plt.subplot(1, 2, 1)
    plt.imshow(I_bin, cmap='gray')
    plt.title('Imagen Binarizada')
    
    # Crea un elemento estructural (disco de radio 5)
    se = disk(5)
    
    # Realiza la operación de apertura
    J = opening(I_bin // 255, se)
    
    # Etiqueta componentes conectados
    L, n = label(J, return_num=True)
    
    # Muestra la imagen procesada y el número de componentes
    plt.subplot(1, 2, 2)
    plt.imshow(J, cmap='gray')
    plt.title(f'Puntos: {n}')
    plt.show()

# Ejecutar la función
morfologia1()
