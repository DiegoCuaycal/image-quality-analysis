import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io, img_as_float

def calcular_nitidez(imagen):
    """Calcular la nitidez usando la varianza del Laplaciano"""
    laplacian_var = cv2.Laplacian(imagen, cv2.CV_64F).var()
    return laplacian_var

def calcular_contraste(imagen):
    """Calcular el contraste usando el rango intercuartílico (IQR)"""
    return np.percentile(imagen, 75) - np.percentile(imagen, 25)

def calcular_ruido(imagen):
    """Calcular el nivel de ruido usando la desviación estándar"""
    return np.std(imagen)

def evaluar_calidad(imagen):
    """Evaluar la calidad de la imagen basada en nitidez, contraste y ruido"""
    nitidez = calcular_nitidez(imagen)
    contraste = calcular_contraste(imagen)
    ruido = calcular_ruido(imagen)
    
    print(f"Nitidez (Laplaciano Var): {nitidez:.2f}")
    print(f"Contraste (IQR): {contraste:.2f}")
    print(f"Ruido (Desv. Estándar): {ruido:.2f}")
    
    # Criterios de calidad
    if nitidez > 100 and contraste > 50 and ruido < 50:
        return "Alta Calidad"
    elif nitidez > 50 and contraste > 30 and ruido < 80:
        return "Media Calidad"
    else:
        return "Baja Calidad"

def mostrar_resultados(ruta_imagen):
    """Mostrar resultados para una imagen"""
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    calidad = evaluar_calidad(imagen)
    
    # Mostrar la imagen y su calidad
    plt.figure()
    plt.imshow(imagen, cmap='gray')
    plt.title(f'Calidad: {calidad}')
    plt.axis('off')
    plt.show()

# Lista de imágenes para probar
imagenes = ['imagen1.jpeg', 'imagen2.jpg', 'imagen3.jpg', 'imagen4.jpeg', 'imagen5.jpg']

# Evaluar y mostrar resultados para cada imagen
for ruta in imagenes:
    print(f"\nEvaluando {ruta}:")
    mostrar_resultados(ruta)
