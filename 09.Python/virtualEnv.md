# Entorno Virtual de Python
 Un entorno virtual es una copia de python local a un proyecto, es una buena practica generar un entorno virtual para cada proyecto apara mantener una misma version de paquetes y version principal de pyhton para el proyecto.

### 1.- Crear entorno
 ``` bash
 python -m venv NombreDelEntorno
 ```

### 2.- Activar entorno
 ``` bash
 source NombreDelEntorno/Scripts/activate
 ``` 

### 3.- Desactivar entorno
  ``` bash
 deactivate
 ``` 

### Guardar dependencias del proyecto
``` bash
 pip freeze > requirements.txt
 ``` 

### Instalar Dependencias del proyecto
 ``` bash
 pip install -r requirements.txt
 ```