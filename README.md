# Biblioteca Django

Este proyecto es una aplicación web desarrollada en Django para la gestión de libros y autores. Permite a los usuarios visualizar libros y autores, y a los usuarios autenticados agregar, editar y eliminar registros.

## Características

- Registro e inicio de sesión de usuarios.
- Página principal.
- Listado y detalle de autores y libros.
- Creación, edición y eliminación de autores y libros (solo para usuarios autenticados).
- API REST para la gestión de libros y autores.

## Tecnologías utilizadas

- Python 3
- Django
- Django REST Framework
- Tailwind CSS (para la interfaz)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/biblioteca-django.git
   cd biblioteca-django
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
5. Crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
6. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

- Acceder a `http://127.0.0.1:8000/` para ver la página principal.
- Registrarse o iniciar sesión para agregar, editar o eliminar libros y autores.
- Acceder a `http://127.0.0.1:8000/api/` para explorar la API REST.

## Estructura del proyecto

El proyecto sigue la siguiente estructura de archivos:

```
project/
│-- myapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│-- project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│-- templates/
|-- db.sqlite3
|-- manage.py
```

## Endpoints de la API

- `GET /api/autores/` - Lista de autores.
- `POST /api/autores/` - Crear un autor (requiere autenticación).
- `GET /api/libros/` - Lista de libros.
- `POST /api/libros/` - Crear un libro (requiere autenticación).

## Plantilla base

La aplicación utiliza Tailwind CSS para la interfaz. La plantilla base (`base.html`) incluye una barra de navegación, autenticación de usuarios y un diseño moderno con colores personalizados.

## Contribución

1. Realizar un fork del repositorio.
2. Crear una rama con la nueva funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Hacer cambios y confirmar:
   ```bash
   git commit -am "Agrega nueva funcionalidad"
   ```
4. Subir los cambios:
   ```bash
   git push origin nueva-funcionalidad
   ```
5. Crear un Pull Request en GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

