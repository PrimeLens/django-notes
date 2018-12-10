

## ELEPHANT SQL

in the virtual env do
```
pip install psycopg2
```
and recreate the listing `pip freeze > requirements.txt`

in settings.py change the following so local server connects to elephant sql<br/>
then afterwards make sure you run migrations and create a superuser
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
into
```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```
example
```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ouefbecks',
        'USER': 'ouefbecks',
        'PASSWORD': 'v3222SSDfsVSFg63GEesgCaYH4443ncOTkm4OOOL',
        'HOST': 'elmo.db.elephantsql.com',
        'PORT': '5432',
    }
```
make sure you run migrations and create a superuser
```
python manage.py migrate
python manage.py createsuperuser
```