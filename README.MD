## Crear el entorno virtual y activarlo

```
python -m venv venv
source venv/Scripts/activate
```

## Instalar librearias

```
pip install django djangorestframework
pip freeze > requirements.txt
```

## Crear el proyecto

```
django-admin startproject reportes_django
cd reportes_django
python manage.py startapp reportes
python manage.py runserver
```

## Luego de crear los models migramos

```
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```