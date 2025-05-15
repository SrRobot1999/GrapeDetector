import torch
import cv2
import numpy as np
from tkinter import Tk, Button, Label, Listbox, Scrollbar, VERTICAL, END
from threading import Thread
from PIL import Image, ImageTk

# Leer el modelo
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/grape_detector_mejorado/model/best.pt')

# Variables globales para controlar la captura de video
cap = None
running = False

# Función para iniciar la videocaptura en un hilo separado
def start_video_capture():
    global cap, running, predictions_listbox
    cap = cv2.VideoCapture(0)
    running = True
    while running:
        ret, frame = cap.read()
        if not ret:
            print("No se puede capturar el video")
            break

        # Realizamos detecciones
        detect = model(frame)
        results = detect.pandas().xyxy[0]  # Obtener predicciones en formato pandas DataFrame

        # Dibujar marco guía
        h, w, _ = frame.shape
        cv2.rectangle(frame, (w//4, h//10), (3*w//4, 9*h//10), (0, 255, 0), 2)  # Marco de enfoque

        # Mostrar la imagen con la detección y el marco
        cv2.imshow('Control de calidad racimo', np.squeeze(detect.render()))

        # Actualizar la lista de predicciones en la interfaz
        predictions_listbox.delete(0, END)  # Limpiar la lista antes de actualizar
        for _, row in results.iterrows():
            label = row['name']  # Nombre del objeto detectado
            confidence = row['confidence']  # Confianza de la predicción
            predictions_listbox.insert(END, f"{label} ({confidence:.2f})")

        # Leer el teclado
        t = cv2.waitKey(5)
        if t == 27:  # 27 es el código ASCII para la tecla 'Esc'
            break

    # Liberar la captura cuando termine
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()

# Función para detener la videocaptura
def stop_video_capture():
    global running
    running = False
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()

# Función para iniciar el hilo de captura
def start_thread():
    capture_thread = Thread(target=start_video_capture)
    capture_thread.start()

# Crear la interfaz gráfica
root = Tk()
root.title("Detector de Uvas")

# Configurar tamaño de la ventana
root.geometry("600x600") 

# Botón para iniciar la videocaptura
start_button = Button(root, text="Iniciar Videocaptura", command=start_thread)
start_button.pack(pady=20)

# Botón para detener la videocaptura
stop_button = Button(root, text="Detener Videocaptura", command=stop_video_capture)
stop_button.pack(pady=10)

# Etiqueta de instrucciones
instructions = Label(root, text="Presione 'Esc' para salir de la videocaptura")
instructions.pack(pady=10)

# Lista de predicciones
predictions_label = Label(root, text="Predicciones:")
predictions_label.pack(pady=10)

scrollbar = Scrollbar(root, orient=VERTICAL)
predictions_listbox = Listbox(root, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=predictions_listbox.yview)
scrollbar.pack(side="right", fill="y")
predictions_listbox.pack(pady=10)

# Añadir logotipo (reemplaza 'logo.png' con la ruta de tu logotipo)
try:
    logo_image = Image.open('logo.jpg')  # Asegúrate de tener un archivo 'logo.jpg'
    logo_image = logo_image.resize((100, 100))  # Redimensiona si es necesario
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(root, image=logo_photo)
    logo_label.photo = logo_photo  # Necesario para mantener una referencia de la imagen
    logo_label.pack(pady=20)
except Exception as e:
    print(f"No se pudo cargar el logotipo: {e}")

# Iniciar la interfaz gráfica
root.mainloop()