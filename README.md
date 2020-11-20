# simple_redirect_website
A simple Django redirect website

## Purpose
Sometimes, we just need to have a simple website so we can redirect traffic somewhere else.
This is helpful when we are moving servers, or migrating a project to another url but need to keep
the old url because users have bookmarked it.

This is a very basic Django version 3 website. The bare minimum. The only purpose is to redirect 
traffic to a specified url.

The goal is to get this up and running under 5 minutes. If you have basic python and django knowledge 
this is very feasible. 

### Pre-requisites
- Python 3.9


Note: If you prefer other version you can change it in the Pipfile.
Change this line.
```
python_version = "3.9"
```

### Windows vs Linux version
This website is to be run on a windows operating system.

For Linux, you will need to exchange 'waitress' implementation with 'gunicorn'

## How to use this
### Setup
- Install all requirements
```
pipenv install
```
- setup the back-end database 
```
cd redirect_website
pipenv run python manage.py makemigrations
pipenv run python migrate
```

The "db.sqlite3" will show in the redirect_website directory

### Run server configuration
- Change the port in the redirect_website/run_server.py to the port you desire. Currently the port is set to 8080
```
PORT = 8080
```

### Error 500 handling
- For proper Error handling message display you must set the debug level to False in the redirect_website\redirect_website\settings.py
```
DEBUG = False
```
- You can change the html text for when an error occurred to any message in the
redirect_website/redirect_website/urls.py

```
html_response = """ ...
```

### Allow hosts
Add the appropriate host that are allowed to server this website.
In the redirect_website/redirect_website/settings.py set the allow_hosts

```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'Your other urls']
``` 

### Start it up
- from a command prompt
```
pipenv run python run_server.py
```
- windows cmd script
Open a windows command prompt and cd to your project.

Your prompt will be something like this "c:\myprojects\simple_redirect_website>"

From that location type:
```
script\windows\start_me.cmd
```
## Test it
From any browser enter 
```
http://localhost:8080
```

if you speficied 8080 as your port in the run_server.py