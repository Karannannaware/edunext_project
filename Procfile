web: gunicorn edunext_project.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn edunext_project.wsgi
