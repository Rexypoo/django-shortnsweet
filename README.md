# shortnsweet

Simple URL shortener app built with [django] 2.0 on [Python] 3

## Getting Started

For detailed instructions on building a django project with this app, refer to [installing](#Installing). If you already have a running django 2.0 project you can clone this app into your project.

_Django writes the file structure into the code, so this app must be cloned inside a folder named 'shortnsweet'._

To activate and incorporate the app perform the following 3 steps:
1. Enable the app in your project `settings.py`
```python
...
INSTALLED_APPS = [
    'shortnsweet.apps.ShortnsweetConfig',
    ...
]
...
```

2. Create a path for short urls in the project `urls.py`
```python
...
from django.urls import include
...
urlpatterns = [
    # Redirect short URLs from directory 't'
    path('t/', include('shortnsweet.urls')),
    ...
]
...
```

3. Add the data model to the project database. At the shell run
```shell
python3 manage.py makemigrations shortnsweet
...
python3 manage.py migrate
...
```

Then you can start your project as normal (`python3 manage.py runserver`) and on the admin page (http://localhost:8000/admin) you can add or remove short URLs. Once you've added a URL alias you can test your short urls at the location defined in `urls.py` during step 2. If you followed the above configuration it would be at http://localhost:8000/t/alias_for_url

By default shortnsweet uses [http status code 302][HTTP 302] temporary redirects. If you ever modify the code to use 301 permanent redirects your browser may cache the redirect, in which case you'll want to try a new alias to ensure the app is working correctly.

### Prerequisites

* [Python 3][Download Python]
    * Python 3.3 or above is recommended for the use of [venv][Virtual environments with venv], but is not required.
* [django][Django] 2.0
    * From the shell `pip3 install django`

### Installing

These steps should provide a working django configuration installed on a Python 3 [virtual environment][Virtual environments with venv].

These instructions will follow many of the steps from [getting started with django] and the [first django app tutorial]. They are excellent resources for anyone new to django.

###### Configuring a virtual environment for your django project

1. Create and navigate to the directory for your project (e.g. `~/src/django`)

2. Create a python virtual environment for the project
```shell
python3 -m venv env
```
_Note that 'env' can be anything, but if you choose a different name you'll need to replace 'env' in the following step._

3. Activate your virtual environment
```shell
source env/bin/activate
```

4. Install django to the virtual environment
```shell
pip3 install django
```

###### Creating a django project

5. Make a django project and navigate into the project directory
```shell
django-admin startproject myshortener
cd myshortener
```
6. __OPTIONAL__: Configure your [database engine][Django engines]. This is beyond the scope of this readme. By default you can leave it alone and django will automatically create a local sqlite database file.

7. Initialize the database so that we can create an administrator
```shell
python3 manage.py migrate
```

8. Create an admin to manage the app
```shell
python3 manage.py createsuperuser
```
_If your server will be accessible from the internet use a strong password._

###### Include the shortnsweet app

9. Clone shortnsweet into your project
```shell
git clone https://github.com/Rexypoo/shortnsweet
```
_Reminder: django uses the path within the code. The app __must__ be in a directory named shortnsweet_

10. Enable the app in your project settings file `myshortener/settings.py`
```python
...
INSTALLED_APPS = [
    'shortnsweet.apps.ShortnsweetConfig',
    ...
]
...
```

11. Create a path for short urls in the project URLs file `myshortener/urls.py`
```python
...
from django.urls import include
...
urlpatterns = [
    # Redirect short URLs from directory 't'
    path('t/', include('shortnsweet.urls')),
    ...
]
...
```
_You can set the path to '' for the shortest urls, but you could have trouble assigning multipurpose URLs like 'admin'_

12. Add the data model to the project database. At the shell run
```shell
python3 manage.py makemigrations shortnsweet
...
python3 manage.py migrate
...
```

13. Start the project server
```shell
python3 manage.py runserver
```

14. Navigate to the admin page (http://localhost:8000/admin), and log in with your superuser credentials from step 7.

15. Select the 'add' option on the line for 'Short urls'. Add any URL and short name of your choice.

Congratulations! The project should perform redirects based on the entries in the 'Short urls' database and the location set by `myshortener/urls.py` (the location set in step 10 is http://localhost:8000/t/).

###### Optionally test the redirector

16. From the [django admin interface][localhost django admin site], add a Short url as follows:
* Url: https://github.com/Rexypoo/shortnsweet
* Alias: shortnsweet_project

17. Visit the url for this redirect at http://localhost:8000/t/shortnsweet_project

You should be redirected to the github page for this app.

## Tests
TODO.

## Deployment

For deployment notes consult with the [django deployment checklist].

The following is required at a minimum:
* Set `DEBUG=False` in the project `settings.py`
* Protect the admin interface
    * Use strong admin passwords
    * Don't send passwords over http
        1. Use https
            * Obtain certificates ([Let's Encrypt] can help)
            * Configure all the necessary [security options]
        or
        2. Only access the admin page from LAN (__never__ from the internet)
            * If using a proxy frontend, don't forward /admin to the internet

## Built With

* [django] 2.0
* [Python]

## Contributing

Please do!
[Fork me on GitHub][Project github page].

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thank you to the [django project][Django]

[HTTP 302]: https://en.wikipedia.org/wiki/HTTP_302
[Download Python]: https://www.python.org/downloads/
[Django]: https://www.djangoproject.com/
[Virtual environments with venv]: https://docs.python.org/3/library/venv.html
[Getting started with django]: https://www.djangoproject.com/start/
[First django app tutorial]: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
[Django engines]: https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-ENGINE
[Localhost django admin site]: http://localhost:8000/admin
[Django deployment checklist]: https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
[Let's Encrypt]: https://letsencrypt.org/getting-started/
[Security options]: https://docs.djangoproject.com/en/2.0/topics/security/#ssl-https
[Python]: https://www.python.org/
[Project github page]: https://github.com/Rexypoo/shortnsweet
[yourls]: http://yourls.org/
