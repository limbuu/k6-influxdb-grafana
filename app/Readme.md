# Project SetUp

## Environment SetUp
```
$ virtualenv venv --python=python3.6
$ source venv/bin/activate
```
## Install libraries/Dependencies
```
$ pip install -r requirements.txt
```
## Install PostgreSQL (Linux/Ubuntu)
Install postgresql following link: https://www.postgresql.org/download/linux/ubuntu/

Now, create a database
```
$ sudo -i -u postgres

postgres@manshi:~$ createdb myapp-db
postgres@manshi:~$ psql myapp-db
psql (13.0 (Ubuntu 13.0-1.pgdg16.04+1))
Type "help" for help.

myapp-db=# 

```
To exit out of postgresql Promt, run command:
```
myapp-db=# \q
```



