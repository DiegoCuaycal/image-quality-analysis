import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops

def dibujar():
    # Captura
    g = cv2.imread('llaves.png')
    
    # Preprocesamiento
    if g is not None and len(g.shape) == 3:  # Es RGB?
        g_gray = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
    else:
        g_gray = g

    # Segmentación (usando el método de Otsu para la binarización)
    T = threshold_otsu(g_gray)
    bw = g_gray < T  # Invertir la binarización para que sea igual a ~bw en MATLAB
    plt.imshow(bw, cmap='gray')
    
    # Etiquetado de regiones
    L = label(bw)
    n = L.max()
    
    # Descripción: obtener el BoundingBox y el Centroid de cada región etiquetada
    stats = regionprops(L)

    # Dibuja el BoundingBox y el Centroid
    plt.figure()
    plt.imshow(bw, cmap='gray')
    plt.title(f'Existen {n} objetos')
    
    for region in stats:
        # BoundingBox
        minr, minc, maxr, maxc = region.bbox
        rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr, 
                             edgecolor='g', facecolor='none')
        plt.gca().add_patch(rect)
        
        # Centroid
        cy, cx = region.centroid
        plt.plot(cx, cy, '+r')
    
    plt.show()

# Ejecutar la función
dibujar()
