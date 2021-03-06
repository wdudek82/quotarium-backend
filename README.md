# Quotarium [Backend]

## Created with:
* python                3.6.5

* pipenv                2018.7.1

* Django                2.0.7
* Django Debug Toolbar  1.9.1
* Django Rest Framework 3.8.2
* Django Rest Swagger   2.2.0
* Django CORS Headers   2.3.0

(complete dependencies list is in Pipfile.lock)

## Setup
* to install all dependencies and create new .venv directory run (in the project's root):
    pipenv install --python python3.6 (you need to have pipenv installed first ofcourse -> pip install pipenv)
* at present stage projects uses only sqlite db, so no further db setup is necessary
* sqlite3 db is included in project's root

## Start application
1. initialize virtual environment: ```pipenv shell```
2. start Django dev server: ```./manage runserver```
3. CORS Headers are set to allow only request comming from localhost:3000,
please see "CORS Headers Settings" in project's settings.py

## Project's URLs:
* Admin Panel: /admin/

* API:
    - ~~/api-auth/~~ auth not used for simplicity sake
    - /api/quotes/
    - /api/authors/

* API Schema (Swagger):
    - /api/schema/
