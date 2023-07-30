# Backend_PracticasIntermedias

* Paso 1:

    - Crear entorno virtual con venv para la gestion de las dependencias a utilizar.

    - python3 -m venv .venv

* Paso 2:

    - Activar el entorno virtual

    - source .venv/bin/activate

* Paso 3: 

    - Intalar todos los paquetes necesarios para el proyecto con la herramienta pip o utilizar el archivo requirements.txt en el entorno de producción de la siguiente forma:
        pip install -r requirements.txt

    Estos son los comandos para instalar las dependencias necesarias para la aplicación de este taller:

    - pip install mysql-connector-python
    - pip install python-dotenv
    - pip install Flask
    - pip install Flask-Cors

* Paso 4:

    - Crear el archivo .env y setear los valores para los parametros de conexión a la instancia de RDS

* Paso 5:

    - Levantar el server
    - python3 server.py


    