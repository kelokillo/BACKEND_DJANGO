# PRUEBA  KALFU BACKEND DJANGO - Gestión de Transporte

Repositorio backend desarrollado en Django para el sistema de gestión de transporte de Kalfu.

Prerrequisitos

* Python 3.10 o superior instalado en tu sistema.
* Git instalado.

Instrucciones de instalación y ejecución

Sigue estos pasos en tu terminal para clonar y poner en marcha el proyecto localmente:

1. Clona el repositorio:
   git clone https://github.com/kelokillo/BACKEND_DJANGO.git
   cd BACKEND_DJANGO

2. Crea un entorno virtual:
   python -m venv venv

3. Activa el entorno virtual:
   - En Windows (PowerShell):
     .\venv\Scripts\Activate
   - En Mac / Linux:
     source venv/bin/activate

4. Instala las dependencias:
   pip install -r requirements.txt

5. Aplica las migraciones de la base de datos:
   python manage.py migrate

6. Inicia el servidor de desarrollo:
   python manage.py runserver

Abre tu navegador e ingresa a http://127.0.0.1:8000/ para ver el proyecto en funcionamiento.