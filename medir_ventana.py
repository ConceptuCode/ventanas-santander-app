import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Función para cargar la imagen usando un cuadro de diálogo
def cargar_imagen():
    # Crear una ventana oculta
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Abrir el cuadro de diálogo para seleccionar una imagen
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
    )
    
    if ruta_imagen:
        # Cargar y procesar la imagen usando OpenCV
        imagen = cv2.imread(ruta_imagen)
        if imagen is not None:
            procesar_imagen(imagen)
        else:
            print("No se pudo cargar la imagen.")
    else:
        print("No se seleccionó ninguna imagen.")

# Función para procesar la imagen y realizar la medición
def procesar_imagen(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque gaussiano para reducir el ruido
    gris = cv2.GaussianBlur(gris, (5, 5), 0)

    # Detección de bordes con Canny
    bordes = cv2.Canny(gris, 50, 150)

    # Encontrar contornos
    contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lista para almacenar posibles contornos del carnet
    contornos_carnet = []

    for cnt in contornos:
        perimetro = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimetro, True)
        if len(approx) == 4:
            area = cv2.contourArea(cnt)
            if area > 1000:  # Ajusta este valor si es necesario
                contornos_carnet.append(cnt)

    if len(contornos_carnet) == 0:
        print("No se encontró el carnet de identidad en la imagen.")
        return

    # Suponemos que el contorno más pequeño es el carnet
    contornos_carnet = sorted(contornos_carnet, key=cv2.contourArea)
    carnet_contorno = contornos_carnet[0]

    # Obtener el rectángulo delimitador del carnet
    x, y, w, h = cv2.boundingRect(carnet_contorno)

    # Dimensiones del carnet en píxeles
    ancho_carnet_px = w
    alto_carnet_px = h

    # Dimensiones reales del carnet (en centímetros)
    ANCHO_CARNET_CM = 8.54
    ALTO_CARNET_CM = 5.4

    # Calcular la escala
    escala_ancho = ancho_carnet_px / ANCHO_CARNET_CM
    escala_alto = alto_carnet_px / ALTO_CARNET_CM
    escala_promedio = (escala_ancho + escala_alto) / 2

    # Suponemos que el contorno más grande es la ventana
    contornos_ventana = sorted(contornos, key=cv2.contourArea, reverse=True)

    for cnt in contornos_ventana:
        perimetro = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimetro, True)
        if len(approx) == 4:
            ventana_contorno = cnt
            break
    else:
        print("No se encontró la ventana en la imagen.")
        return

    # Obtener el rectángulo delimitador de la ventana
    x, y, w, h = cv2.boundingRect(ventana_contorno)

    # Dimensiones de la ventana en píxeles
    ancho_ventana_px = w
    alto_ventana_px = h

    # Calcular dimensiones en centímetros
    ancho_ventana_cm = ancho_ventana_px / escala_promedio
    alto_ventana_cm = alto_ventana_px / escala_promedio
    print(f"Ancho de la ventana: {ancho_ventana_cm:.2f} cm")
    print(f"Alto de la ventana: {alto_ventana_cm:.2f} cm")

    # Dibujar contorno del carnet en verde
    cv2.drawContours(imagen, [carnet_contorno], -1, (0, 255, 0), 2)

    # Dibujar contorno de la ventana en rojo
    cv2.drawContours(imagen, [ventana_contorno], -1, (0, 0, 255), 2)

    # Mostrar la imagen con los contornos
    cv2.imshow('Detección', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejecutar la carga y procesamiento de la imagen
if __name__ == "__main__":
    cargar_imagen()