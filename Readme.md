**SignAds API platform MVP**

A B2B SaaS platform where ads will be crafted such that user click rate and interaction will be increased.

The platform is primarily based on our proprietary persuasion algorithm.

For the list of various APIs that have been implemented, please refer APIs.md file.

For executing server code please execute the following steps on your command console:

~~~
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver <port-number>
~~~

Note: Also please make sure that 
~~~ 
db.sqlite and other migration files 
~~~ 
are deleted before each time the server starts running for demo purposes.

Also please make sure that all the respective paths are set properly according to your system.

After future releases, such conflicts will be resolved.