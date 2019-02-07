This folder of notes needs review.<br/>
A working app has been dropped in here as a temporary replacement.

- copy folder into code
- add the app in the settings.py


- Cors needs to be added https://pypi.org/project/django-cors-headers/<br/>
  `CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?ferryworth\.com$', )`
- `pip freeze > requirements.txt`
- eb deploy (env name)


## URLS 

If the django app is at 
- https://app.mydomain.com

REST endpoint will be at 
- https://app.mydomain.com/api/v2/

Backend Interface
- login will be https://app.mydomain.com/admin
- users list will be https://app.mydomain.com/admin/auth/user/
- lookouts list will be https://app.mydomain.com/admin/lookout/lookout/
