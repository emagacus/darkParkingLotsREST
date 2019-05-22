web: gunicorn myproject.wsgi
release: python tutorial/manage.py migrate
