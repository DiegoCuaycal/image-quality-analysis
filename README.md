# 🖼️ Procesamiento de Imágenes - Segmentación, Morfología y Evaluación de Calidad

Este proyecto presenta un conjunto de scripts de **procesamiento de imágenes** implementados en Python, enfocados en el análisis básico de imágenes a través de técnicas de **visión por computador**. Se aplican métodos como **segmentación por umbral adaptativo**, **operaciones morfológicas**, **detección de orientación** y **evaluación de calidad de imágenes** utilizando métricas estadísticas.

## 📂 Estructura del Proyecto

- `dibujar.py`: Segmentación de imagen, detección de objetos, dibujo de bounding boxes y centroides.
- `morfologia1.py`: Procesamiento morfológico mediante apertura para eliminar ruido y contar objetos.
- `orientacion_img.py`: Cálculo de la orientación de objetos en imágenes y rotación para alineación horizontal.
- `evaluar_calidad_imagenes.py`: Evaluación automática de nitidez, contraste y ruido para clasificar la calidad de imágenes.

## 🚀 Tecnologías utilizadas

- Python 3.11+
- OpenCV
- NumPy
- Matplotlib
- scikit-image
- SciPy

## 🛠️ Instalación

```bash
# Clonar el repositorio
$ https://github.com/DiegoCuaycal/image-quality-analysis.git
$ cd image-quality-analysis

# Instalar dependencias
$ pip install -r requirements.txt
```

Contenido sugerido para `requirements.txt`:

```text
numpy
opencv-python
matplotlib
scikit-image
scipy
```

## ⚡ Ejecución

Cada script es independiente y puede ejecutarse directamente.  
Ejemplo para correr un script:

```bash
python dibujar.py
```

**Nota:** Asegúrate de tener las imágenes necesarias en la misma carpeta o ajustar las rutas en el código:
- `llaves.png`
- `puntos_lineas.jpg`
- `pieza-1.png`
- `imagen1.jpeg`, `imagen2.jpg`, etc.

## 📋 Descripción de las Funciones

| Script | Funcionalidad Principal |
|:------:|:------------------------|
| `dibujar.py` | Segmenta objetos y dibuja cajas y centroides sobre ellos. |
| `morfologia1.py` | Realiza apertura morfológica para limpiar ruido y contar elementos. |
| `orientacion_img.py` | Detecta la orientación de un objeto y rota la imagen para alinearlo. |
| `evaluar_calidad_imagenes.py` | Evalúa imágenes en términos de nitidez, contraste y ruido, clasificándolas en alta, media o baja calidad. |

## ✨ Características destacadas

- Uso de umbralización de Otsu para segmentación automática.
- Procesamiento morfológico clásico (apertura, cierre).
- Cálculo de propiedades geométricas (bounding box, centroide, orientación).
- Evaluación estadística de calidad de imágenes basada en métricas objetivas.


