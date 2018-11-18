# CURRENTLY UPGRADING 
# Notes to Django 1.11 Python 3.6 (was django 1.8 python 2.7)
1.11 taken from udemy django ecommerce
1.8 taken from Up & Running with Django by Caleb Smith

Install Python 3.6, Virtualenv, & Django on Mac [link](https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux/)
Python resources [link](https://github.com/codingforentrepreneurs)

## Basics


```
brew install python            installs python 3
brew install python@2          installs python 2.7
python3 -V                     gets version
pip --version                  python installer of packages,  to get the version of pip
pip3 --version
pip3 install <package>
sudo pip install virtualenv    this is virtual within the confines of a directory
virtualenv --version

PROJECT SETUP
virtualenv -p python3 .        Do this in the project folder,  sets up python3 for that project
source activate                Do this in project folder / bin (to activate shell and prompt will change)
deactivate                     Do this in project folder / bin
source bin/activate            Or do this in project folder

Within the virtual env you can do the following (indented to show we are in the virtualenv shell)
  pip install django==1.11
  django-admin --version       to check django is installed
  mkdir src                    this is important because startproject creates a /bin which overwrite the one made by vitualenv
  cd src                        
  django-admin startproject djangomyproj
                               starts a project called 'djangomyproj'
                               you now have manage.py and a folder called 'djangomyproj'
  python mamage.py             runs the manage.py file and it displays a list of sub commands
  python mamage.py <subcommand>
                               runs django subcommand, for example runserver 
```

`python manage.py runserver` will start a server at 127.0.0.1:8000 (localhost:8000) and this will work immediately after creating a project _but it kicks an error prompting a migration but thats ok_

```
__init__.py         tells it that its a python module (often called the 'dunder' init)
wsgi.py             used by webserver to run the proj (often called the 'wazgi' init)
urls.py             is the config for serverside router
```

## Django Apps within a Django project
Django 'app' terminology. In the django world an 'app' is a folder with a set of related python files in it, more like a component. A Django project can have multiple apps within it. Each app tends to have a specific purpose for example blog app or forum app and they have a certain structure within their app folder
  - `models.py`         defines data layer (structure of DB tables and how they are queried)
  - `admin.py`          administrative interface (admin for read or update of db tables)
  - `views.py`         control layer (and routing)
  - `tests.py`          tests
  - `migrations/`       folder to hold migrations

## Use the django subcommand to create an app in the django project

```
python manage.py startapp myfirstapp
```

This creates a folder within the project, but it is not yet included in the binary compile<br/>
<img src="./images/1.png" width="50%"/><br/>
To include it open `djangomyproj/djangomyproj/settings.py` and scroll to `INSTALLED_APPS = (` and add myfirstapp like this<br/>
<img src="./images/2.png" width="25%"/><br/>

To rename an app there are two places to change.
- the name of the folder 'myfirstapp'
- in the settings.py the above line 40 'myfirstapp'

## The django docs for settings

Find them by going to djangoproject.com click top nav link for documentation, scroll a third of the way down page to subheading The Development Process and under it are some bullets, the first bullet is called Settings and click the Overview link next to it<br/>
<img src="./images/3.png" width="25%"/><br/>
We already edited a setting above to add myfirstapp app into the compile. If you need to use serverside templating in django you would edit `TEMPLATES = [` in the same file.Other settings commonly altered are static files directory, debug and databases. Check the docs link.

## Models
- each app has a models.py define your classes in there
- classes inherit from django.db.models

In `/myfirstapp/models.py` define the class like this

```
class Item(models.Model):
  title = models.CharField(max_length=200)  # must have max_length
  description = models.TextField()   
  amount = models.IntegerField()            # -1, 0, 1, 20
  amount = models.PositiveIntegerField()
  weight = models.DecimalField(decimal_places=2, max_digits=5)
                                            # 0.5, 3.14
  is_new = models.BooleanField()            # True, False
  date_sold = models.DateTimeField()        #   
  email = models.EmailField()               # george@email.com
  url = models.URLField()                   # www.google.com
  docs = models.FileField()                 # user_uploaded.doc
  pic = models.ImageField()                 # best_avatar.jpg
  owner_id = models.PositiveIntegerField(default=0)
```

```
  title = models.CharField(max_length=10, null=True, blank=True)
  # null is an accepted value that can be stored
  # blank means an empty string is accepted
  # default sets a default
  # choices can set delimeters or guard rails on the values
```

## Migrations

Adding the class in models.py doesn't create the table, to do that you need to use a migration. Migrations will add a model, add a field, remove a field or change the attributes of a field

```
  python manage.py makemigrations
```

- generates migration files for later use, these are stored in the app folder example '/myfirstapp/0001_initial.py'
- compares the current model fields against the current database tables
- do this from the top level above the app folder

```
  python manage.py migrate
```

- runs all migration files that have not been run yet

```
  python manage.py migrate --list
```

- see all the migrations for different apps and which ones have been run (unapplied migrations is the name for those that havent run yet)


## View the data in sqlitebrowser
- download from http://sqlitebrowser.org/ the way I did this was with<br/> 
  `brew cask install db-browser-for-sqlite`
- run the new application DB Browser for SQlite, it should now be in your applications folder
- use it to open the file `db.sqlite3` which is in the main proj folder (above the app folders)
- you will see many tables but the one you want is named appname + underscore + tablename<br/>
  example: `myfirstapp_item`

## Register the item model with django admin
- open admin file in app folder `Project > App > admin.py` and then if your model class is called `Item` you would add 

```
  from .models import Item
  admin.site.register(Item)
```

## Create Super User for web interface login
- user terminal to go to top level project folder, this is the folder with `manage.py` and run

```
  python manage.py createsuperuser
  # note: will prompt for username, email and password and its ok to leave email blank
```

- then do `python manage.py runserver` and in the browser url put `http://localhost:8000/admin` then login
- here you can add items to the DB table and view the rows, the row view is not helpful, see next section

## Django out-of-the-box "List Display Page" is crap, lets fix it
<img src="./images/4.png" width="50%"/><br/>

- to make the row view more useful modify the lines from `Project > App > admin.py` so it looks like this

```
  from .models import Item 
  class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'weight']
  admin.site.register(Item, ItemAdmin)
```

<img src="./images/5.png" width="50%"/><br/>
- click on the item to edit it, use the drop down to delete it

## What is Django ORM
- stands for Object Relational Mapper
- maps database columns to python objects

## Using Django shell
- user terminal, make sure you are in top level of project, type `python manage.py shell` and prompt will now look like `>>>`
- from the `>>>` prompt type 

```
  from myfirstapp.models import Item
  #from <app_name>.models import <class_of_model>
```

- then try the following

```
  Item.objects.all()
  # [<Item: Item object>, <Item: Item object>, <Item: Item object>, <Item: Item object>]
  itemsList = Item.objects.all()
  item = itemsList[0]
  item.title
  item.description
  item.id
```

- using the getter

```
  item = Item.objects.get(id=2)
  itemList = Item.objects.filter(weight=2)   # all with weight 2
  itemList = Item.objects.exclude(weight=2)  # all with weight not equal to 2
```

## Django serverside router (empty route)

- open the django app folder that has the _same name_ as the project and open `urls.py` 
- this is the default

```
  urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
  ]
```

- we added a line for the url and a line to import the views from the app we created

```
  # import views from the app we created
  from myfirstapp import views 

  urlpatterns = [
    # '^$' is regex for empty string see below
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
  ]
```

- and most importantly we must go into project folder > app folder > `views.py` and added

```
  from django.http import HttpResponse
  def index(request):
    return HttpResponse('<p>hello world<p/>')
```

- http://localhost:8000/ now shows hello world

Regex screenshot taken from the course, use https://pythex.org/ to test<br/>
<img src="./images/6.png" width="50%"/><br/>
1st - ducky matches to anywhere in the string<br/>
2nd - \d is only a single digit character<br/>
3rd - \d+ will match to one or more digit characters<br/>
4th - ^ means the string must start with admin/<br/>
5th - similarly $ suffix is the same as ^ except for the end<br/>
6th - this is how to match an empty string<br/>


## Django serverside router (define and pass variable)

- open the django app folder that has the _same name_ as the project and open `urls.py` 
- add line

```
  # define variable named id
  url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
```

- in project folder > app folder > `views.py` add the following

```
  def item_detail(request, id):
    return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
```

- http://localhost:8000/item/1/ now shows 'In item_detail view with id 1'

## Connecting templates with dynamic data to the router

  - following from the above example, in project folder > app folder > `views.py` delete import for HttpResponse object as it is no longer needed
  - instead add `from django.http import Http404`
  - and add the item model from myfirstapp.models so we can use it to query the DB <br/>
    `from myfirstapp.models import Item`
  - swap out code for def index


```
  def index(request):
    return HttpResponse('<p>hello world<p/>')

  # CHANGE TO THIS

  def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
      'items': items,     # note here var name is plural
    })
```

  - swap out code for def item_detail

```
  def item_detail(request, id):
    return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))

  # CHANGE TO THIS

  def item_detail(request, id):
    try:
      item = Item.objects.get(id=id)
    except Item.DoesNotExist:
      raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
      'item': item,     # note here var name is singular
    })
```

  - open the django app folder that has the _same name_ as the project and open `settings.py` and look for the templates variable that looks like this `TEMPLATES = [{}]` and add in path to templates which in this tutorial is storing all templates in the _same name app_.  I know this is confusing and stupid but the settings.py file in the lower level app is using a relative path fom the project folder root so think of it like<br/>
  `'djangomyproj/djangomyproj/templates'` or <br/>
  `'./djangomyproj/templates'`<br/>
  but the way django wants it written is

```
  TEMPLATES = [ 
    { 
      DIRS : ['djangomyproj/templates'] 
    } 
  ]
```

  - You can then go to project folder > app folder with same name > templates and add 'index.html' and 'item_detail.html' each with just `<p>hello world</p>` if you want to see it running or use the next section to render dynamic data

## Template Tags

```
  <h3>{{ headline_name }}</h3>

  {% for item in items %}
    <p>{{  item.title }}</p>
  {% endfor %}

  # in the router file urls.py we specified name='index' and name='item_detail' this is useful in the 
  # template but note if a url regex pattern has any name groups they will need to be included
  <p>{% url 'index' %}</p>                      # url(r'^$', views.index, name='index')
  <p>{% url 'item_detail' item.id %}</p>        # url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail')

  # Filters can be used
  <p>{{ item.name|capfirst }}</p>

  # parent templates/base.html
  <body>
    {% block content %}
    {% endblock content %}
  </body>

  # child templates/myfirstapp/index.html
  {% extends "base.html" %}
  {% block content %}
      <h3>Items in stock</h3>
      <ul>
        {% for item in items %}
          <li>
            <a href="{% url 'item_detail' item.id %}">
              {{ item.title|capfirst }}
            </a>
          </li>
        {% endfor %}
      </ul>
  {% endblock %}

  # child templates/myfirstapp/item_detail.html
  {% extends "base.html" %}
  {% block content %}
    <a href="{% url 'index' %}">Back to item list</a>
    <h3>{{ item.title|capfirst }}</h3>
    <p> {{ item.amount }} currently in stock</p>
    <h4>Description:</h4>
    <p> {{ item.description }}</p>
  {% endblock %}

  # for static assets look up docs to define ststic path in swttings.py
  then in templates <link rel="stylesheet" href="{% static 'main.css' %}">
```

<hr/>


### Additional:

Taken from Advanced Django by Kevin Veroneau and Matthew Nuzum 
Uses python 2.7 and django 1.8

what is middleware?
I like the definition from Matthew Nazum (lynda) he says "middleware is code that hooks into the request response cycle of a page view" and he said this in Advanced Django course

Standard as of Oct 2017
  - Django 1.11 is the standard, it uses python 2.7,  it is the last django to use 2.7
  - in Dec 2017 Django 2 will be released that uses python 3 and it will most likely be a rough start

django 1.11 docs on auth
https://docs.djangoproject.com/en/1.11/topics/auth/default/

tastypie  is what is referenced in Advanced Django course and its github claims support with 1.11 also it has high user traction,  it might be good until django 2.0 comes out


