
## When your app is hosted it is likely the /admin pages will have no css

- go to `settings.py` and add the following

```
STATIC_URL = '/static/'
# https://stackoverflow.com/questions/28728912/django-admin-site-not-showing-css-style
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- make sure you added the above lines first<br/>
  then make while in the virtual environment do `python manage.py collectstatic`
- do git commits and redeploy
