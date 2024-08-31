# Blog django

Creacion de una pagina web simulando una pagina estilo blog creada a partir de django y html

## Funcionalidades

Aquí encontras las principales funciones que se han implementado en el proyecto:

- **Funcionalidad 1**: Se crea vista de inicio con enlaces a demas vistas (listar post y agregar post)
- **Funcionalidad 2**: Se crea vista para listar los post publicados
- **Funcionalidad 3**: Se crea formulario de creacion y actualizacion de post (este ultimo se accede desde la vista de detalle)
- **Funcionalidad 4**: Se crea vista de detalle para cada post
- **Funcionalidad 5**: Se implementan filtros por fecha, categoria, nombre y contenido

## Instalación

Pasos para instalar el proyecto localmente:

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/velasquezgalejandro/blog-django.git
    ```

2. **Accede al directorio del proyecto:**

    ```bash
    cd blog-django
    ```

2. **Accede a la carpeta principal:**

    ```bash
    cd blog
    ```

3. **Ejecuta las migraciones de la base de datos e inicia el servidor en local:**
    ```bash
    python manage.py makemigration
    python manage.py migrate
    python manage.py runserver
    ```

    o

    ```bash
    py manage.py makemigration
    py manage.py migrate
    py manage.py runserver
    ```
