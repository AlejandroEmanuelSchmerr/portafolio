
# Portafolio Personal

Este es un portafolio personal desarrollado con Django, Python, HTML, CSS y SQLite3. No es mi portafolio definitivo, pero es una muestra funcional de mis habilidades en desarrollo web.

---

## Características

- **Portada:** Página principal que muestra mi nombre y una foto personal.  
- **Acerca de:** Información sobre mí, mi educación, formación, y habilidades, acompañada de un ícono decorativo.  
- **Proyectos:** Listado de proyectos con nombre, descripción, tecnologías, estado, imagen y un enlace al repositorio del proyecto.  
- **Contacto:** Formulario funcional para enviar mensajes.  
- **Diseño consistente:** Todas las páginas tienen un menú de navegación y un footer con enlaces a mis redes sociales.  

Los proyectos son gestionados desde el panel de administración de Django (superusuario) y almacenados en una base de datos SQLite3 (`db.sqlite3`).

---

## Requisitos Previos

1. **Python 3.9 o superior**  
   Descárgalo desde [python.org](https://www.python.org/).

2. **Django**  
   Instálalo con:
   ```bash
   pip install django
   ```

3. **DB Browser for SQLite**  
   Descárgalo desde [sqlitebrowser.org](https://sqlitebrowser.org/) para abrir y administrar la base de datos.

4. **Visual Studio Code (VS Code)**  
   Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/).

---

## Instalación y Configuración

### 1. Descargar los Archivos
1. Descarga el archivo ZIP del proyecto desde el repositorio.
2. Extrae el archivo ZIP en una carpeta de tu elección.

### 2. Configurar la Base de Datos con DB Browser for SQLite
1. Abre **DB Browser for SQLite**.
2. Haz clic en **Abrir Base de Datos**.
3. Busca y selecciona el archivo `db.sqlite3` incluido en el proyecto.
4. Cierra el programa una vez que hayas confirmado que la base de datos está correctamente configurada.

### 3. Instalar Dependencias
1. Abre la terminal y navega a la carpeta donde descomprimiste los archivos:
   ```bash
   cd ruta/del/proyecto
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
   *(Si no hay un archivo `requirements.txt`, asegúrate de instalar Django manualmente).*

### 4. Ejecutar el Servidor
1. Inicia el servidor con:
   ```bash
   python manage.py runserver
   ```
2. Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver el proyecto.

### 5. Acceso al Panel de Administración
1. Visita [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
2. Ingresa con las credenciales del superusuario (creadas previamente) para cargar y administrar proyectos.

---

## Autor

- **Emanuel Schmer**  
  **Correo:** [emanuelschmer@hotmail.com](mailto:emanuelschmer@hotmail.com)  

---

## Agradecimientos

Gracias por tomarte el tiempo de revisar este proyecto. ¡Espero que lo encuentres interesante y útil! 😊
