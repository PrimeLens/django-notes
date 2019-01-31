
If you had a python file `fred.py` in an app (or folder) called `arcticmonkeys` containing the following

```
FRED = ['hello', 'goodbye']
```

You can import like this 
```
from arcticmonkeys.fred import * 
```

Or conditionally import like this

```
if myenv=='production':
    from arcticmonkeys.fred import * 
```

This results in the code being included

Note that `arcticmonkeys` does not have to be an app and can be a folder
