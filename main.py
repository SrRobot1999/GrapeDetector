# Importar las librerías
import torch 
import cv2
import numpy as np

# Leer el modelo
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/grape_detector_mejorado/model/best.pt')

# Realizar videocaptura
cap = cv2.VideoCapture(0)

# Empezamos
while True:
    # Realizamos la lectura de la videocaptura
    ret, frame = cap.read()
    
    if not ret:
        print("No se puede capturar el video")
        break

    # Realizamos detecciones
    detect = model(frame)

    # Mostramos FPS
    cv2.imshow('Control de calidad racimo', np.squeeze(detect.render()))

    # Leemos el teclado
    t = cv2.waitKey(5)  # Cambiado a waitKey con "K" mayúscula
    if t == 27:  # 27 es el código ASCII para la tecla 'Esc'
        break

# Liberar la captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()