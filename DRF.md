

## VirtualBox and Vagrant

get virtualbox from virtualbox.org
get vagrant from vagrantup.com
  after install type `vagrant version` to check it is installed

get a python .gitignore from  https://github.com/github/gitignore/blob/master/Python.gitignore

do `vagrant init` when in the project folder

get a vagrant file from the course from here https://gist.github.com/LondonAppDev/d990ab5354673582c35df1ee277d6c24

## DRF

pip install djangorestframework==3.7.7

got to settings.py an add `rest_framework` and `rest_framework.authtoken`


```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
]

```

## Save the required python libraries

`pip freeze > requirements.txt`

## create a django app called profiles_api



