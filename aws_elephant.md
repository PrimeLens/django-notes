

## ELEPHANT SQL BASIC CONNECTION

in the virtual env do
```
pip install psycopg2
# https://pypi.org/project/psycopg2/
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
source ../bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## AWS ENV PROPERTIES WITH ELEPHANTSQL STAGING AND PRODUCTION  

The above code shows a basic connection but does not solve
- staging database vs production database
- security of avoiding committing keys to git

It is far better to use environment properties in AWS to hold the connection URL so 

1. In /src of your project install this python library and update requirements.txt

```
pip install dj-database-url
# https://github.com/kennethreitz/dj-database-url
pip freeze > requirements.txt
```

2. Go to the AWS environment Configuration > Software > Environment Properties and add `db_url` as the key and the url connection string as the value. Do this for each environment

3. In `settings.py` edit the DATABASES= to the following

``` 
# set up local postgres as a default
db_url = 'postgres://hello@localhost:5432/hello'
# db_url = `postgres://ghijk:aBcDeFgHiJ@pellefant.db.elephantsql.com:5432/ghijk`

# check for an environment property from AWS or other hosting
if os.environ.get('db_url') is not None:
  db_url = os.environ['db_url']

# parse the connection string into the properties needed for django DATANASES dictionary
import dj_database_url
DATABASES = {
    'default': dj_database_url.parse(db_url)
}
``` 



Reference https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-container.html

## Alternatively you can set up a local postgres
- [local postgres](./local_postgres.md)
