import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.morphology import binary_closing
from skimage.measure import label, regionprops
from scipy.ndimage import rotate

def orientacion_img():
    # Captura
    g = cv2.imread('pieza-1.png')

    # Preprocesamiento
    if g.shape[2] == 3:  # ¿Es RGB?
        g_gray = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
    else:
        g_gray = g

    # Mostrar la imagen original en escala de grises
    plt.subplot(2, 2, 1)
    plt.imshow(g_gray, cmap='gray')
    plt.title('Imagen Original')
    
    # Segmentación (usando el método de Otsu para la binarización)
    umbral = threshold_otsu(g_gray)
    bw = g_gray > umbral
    plt.subplot(2, 2, 2)
    plt.imshow(bw, cmap='gray')
    plt.title('Imagen Binarizada')
    
    # Rellenar los huecos en la imagen binaria
    bw2 = binary_closing(bw)
    plt.subplot(2, 2, 3)
    plt.imshow(bw2, cmap='gray')
    plt.title('Relleno de Huecos')
    
    # Descripción de la imagen
    labeled_img = label(bw2)
    props = regionprops(labeled_img)
    
    if len(props) > 0:
        orientation = props[0].orientation  # Obtiene la orientación en radianes
        angle_deg = -orientation * (180 / np.pi)  # Convierte de radianes a grados
        
        # Rotar la imagen para alinear con el eje horizontal
        Ir = rotate(bw2, angle_deg)
        plt.subplot(2, 2, 4)
        plt.imshow(Ir, cmap='gray')
        plt.title(f'Rotada: {angle_deg:.2f}°')
    
    plt.tight_layout()
    plt.show()

# Ejecutar la función
orientacion_img()
