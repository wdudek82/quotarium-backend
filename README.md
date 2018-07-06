# Quotarium [Backend]

## Created with:
* python                3.6.1

* pipenv                5.0.0

* Django                2.0.7
* Django Debug Toolbar  1.8.0
* Django Rest Framework 3.6.3
* Django Rest Swagger   2.1.2

(complete dependencies list is in Pipfile.lock)

## Setup
* to install all dependencies and create new .venv directory run (in the project's root):
    pipenv install --python python3.6 (you need to have pipenv installed first ofcourse -> pip install pipenv)
* at present stage projects uses only sqlite db, so no further db setup is necessary
* sqlite3 db is included in project's root


## Project's URLs:
* Admin Panel: /admin/

* API:
    - ~~/api-auth/~~ auth not used for simplicity sake
    - /api/quotes/
    - /api/authors/

* API Schema (Swagger):
    - /api/schema/