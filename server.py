import os
from logger_settings import api_logger

try:
    if os.path.exists("db.sqlite3"):
        os.system("del db.sqlite3")
        os.system("python server.py")
        api_logger.info("Server has started running...")
    else:
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate --run-syncdb")
        os.system("python manage.py runserver")
        api_logger.info("Server has started running...")

except Exception as e:
    api_logger.exception("Exception occurred in running server..."+str(e))

