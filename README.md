## This project was made with:

* [Python 3.10.2](https://www.python.org/)
* [Django 3.2.11](https://www.djangoproject.com/)  

## how to run the project?

* Create a virtualenv with Python 3.
* Activate virtualenv.
* Install dependencies.
* Run migrations.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

The application will be running on port 8000.
