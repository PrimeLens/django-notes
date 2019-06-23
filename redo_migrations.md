## Redoing migrations

Using my localhost DB as a testing ground I ran a migration that created a table then I wanted to undo that. Luckily for me it was the first migration for that app and I used 

```
python manage.py migrate <app name> zero
```

and checking postgres through terminal the table was gone.

There are ways to migrate to a specific point in the history of that app like a git reversion using 

```
python manage.py migrate <app name> <migration name>
# then delete the migration file
```

[stack link](https://stackoverflow.com/questions/32123477/django-revert-last-migration) 

