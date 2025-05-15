# Grape Detector Mejorado

Este proyecto es una aplicación para la detección de uvas utilizando modelos de aprendizaje profundo. Incluye una interfaz gráfica y utiliza modelos personalizados para la detección.

## Requisitos

- Python 3.8 o superior (se recomienda usar un entorno virtual)
- Git
- pip

## Clonar el repositorio

Abre una terminal y ejecuta:

```sh
git clone https://github.com/SrRobot1999/GrapeDetector.git
cd GrapeDetector
```

## Crear y activar un entorno virtual

**Windows:**
```sh
python -m venv env
env\Scripts\activate
```

**Linux/MacOS:**
```sh
python3 -m venv env
source env/bin/activate
```

## Instalar dependencias

Asegúrate de tener `pip` actualizado:

```sh
python -m pip install --upgrade pip
```

Instala las dependencias principales (ajusta el nombre del archivo si tienes un requirements.txt):

```sh
pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, instala manualmente las dependencias principales (ejemplo):

```sh
pip install ultralytics opencv-python PyQt5 torch torchvision
```

## Archivos y carpetas importantes

- `main.py`: Script principal para ejecutar la aplicación.
- `interfaz.py`: Código de la interfaz gráfica.
- `model/best.pt`: Modelo entrenado para la detección.
- `model/custom.yaml`: Configuración del modelo.
- `logo.jpg`: Imagen utilizada en la interfaz.
- `build/`: Carpeta generada por PyInstaller para la distribución.
- `env/`: Entorno virtual (no es necesario subirlo al repositorio).

## Ejecución

Con el entorno virtual activado, ejecuta:

```sh
python main.py
```

o, si la interfaz principal está en otro archivo:

```sh
python interfaz.py
```

## Exportar como ejecutable (opcional)

Si deseas crear un ejecutable con PyInstaller:

```sh
pip install pyinstaller
pyinstaller --onefile --windowed interfaz.py
```

El ejecutable se generará en la carpeta `dist/`.

## Notas

- Asegúrate de que el archivo del modelo (`model/best.pt`) esté presente en la ruta correcta.
- Si tienes problemas con dependencias, revisa la versión de Python y reinstala los paquetes necesarios.
- Para actualizar el repositorio, usa:
  ```sh
  git pull origin main
  ```

---

¡Listo! Ahora puedes usar y modificar el proyecto según tus necesidades.