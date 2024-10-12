Ventanas Santander App

Este es un proyecto para una aplicación de medición de ventanas desarrollada para Ventanas Santander. La aplicación permite a los usuarios subir una imagen de una ventana con una tarjeta de referencia (como un carnet de identidad) para calcular las dimensiones exactas de la ventana sin necesidad de visitar físicamente el domicilio.

Características principales:

Subida de imágenes: Los usuarios pueden subir una imagen de la ventana que desean medir.

Procesamiento de imagen con OpenCV: La aplicación utiliza OpenCV para identificar la tarjeta de referencia y calcular el tamaño de la ventana.

Interfaz responsiva: El diseño se adapta a todos los dispositivos, asegurando una buena experiencia en móviles y escritorio.

Despliegue en PythonAnywhere.


Estructura del Proyecto:

app.py: Archivo principal de la aplicación, construido con Flask.

templates/: Carpeta que contiene los archivos HTML para la interfaz de usuario.

static/: Carpeta para almacenar los archivos CSS y JavaScript estáticos.

uploads/: Carpeta donde se almacenan las imágenes subidas por los usuarios.

requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto (Flask, OpenCV, etc.).


Requisitos previos:

Python 3.x

Flask

OpenCV

NumPy


Instrucciones de instalación:

1. Clonar el repositorio:

git clone https://github.com/ConceptuCode/ventanas-santander-app.git


2. Crear un entorno virtual y activarlo:

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate


3. Instalar las dependencias:

pip install -r requirements.txt


4. Ejecutar la aplicación:

python app.py


5. Acceder a la aplicación: Abre tu navegador y ve a http://127.0.0.1:5000 para usar la aplicación localmente.



Despliegue:

Este proyecto está configurado para ser desplegado en PythonAnywhere. Para desplegarlo desde un repositorio de GitHub:

1. Clona el repositorio en PythonAnywhere.


2. Configura el entorno virtual y las dependencias necesarias.


3. Configura el archivo app.py como punto de entrada en la configuración de la aplicación web.
