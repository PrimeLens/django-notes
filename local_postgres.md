## Referencing
- instructions here https://postgresapp.com/


## How to create a local postgres

- open postgress app (blue elephant)
- click initialize (the server is now running)
- add to the os path (similar to editing bash profile)
```
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```
- you now have postgres at the following connection details

```
Host	localhost
Port	5432
User	same as osx user
Database	same as osx user
Password	none
Connection URL	postgresql://localhost
```

## Full Connection URL (note no password) for Django
```
postgres:// (username) : (password) @ (DB instance id + endpoint) : (port=5432) / (database name)
postgres://osxuser@localhost:5432/osxuser
```

## PSQL connection for a quick check from a terminal
`psql -h localhost -U osxuser -d osxuser`
`\q` to quit



