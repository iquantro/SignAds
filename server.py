import os

if os.path.exists("db.sqlite3"):
    os.system("del db.sqlite3")
    os.system("python server.py")
else:
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate --run-syncdb")
    os.system("python manage.py runserver")
    print("platform is up and running...")

