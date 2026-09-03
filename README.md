# EventsApp - Sistema de Gestión de Reservas de Eventos
Desarrollado en Django para Alkemy 2026 - Grupo número 1

---

### Requisitos
Tener instalados Python y Git.
* **Python 3.10+**
* **Git**

  ---

## Instrucciones de instalación y puesta en marcha.

### 1. Clonar el respositorio
  
  ```bash
  git clone https://github.com/PonceDiego/eventos
  cd eventos
  ```

### 2. Crear y activar entorno virtual
* Windows (PowerShell/CMD)
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* Linux/MacOS
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

 ### 3. Dependencias
  Instalar las dependencias necesarias
    ```bash
    pip install -r requirements.txt
    ```
### 4. Migraciones
  Migrar las estructuras de la base de datos
  ```bash
  python manage.py migrate
  ```
### 5. Crear Superusuario
  Usuario para acceder a Django Admin (/admin)
```bash
python manage.py createsuperuser
```
### 6. Poblar Base de datos
  Script de carga masiva para generar registros iniciales (Clientes, Servicios, Empleados, Coordinadores y Reservas)
```bash
python seed_data.py
```
> [!TIP]
> También se puede correr a través del shell de Django con `python manage.py shell < seed_data.py`.

### 7. Iniciar Servidor
```bash
python manage.py runserver
```
### 8. Visitar Web
  Abrir el navegador y acceder a http://127.0.0.1:8000/

## Estructura del proyecto
* `servicios/`: Aplicación principal.
* `api/`: Endpoints disponibles (Django-REST).
  
