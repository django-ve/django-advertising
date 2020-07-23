Django-Advertising
==================

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |django30x-docs| |help|
    * - tests
      - | |python37| |django30x| |travis| |coverall|
    * - license
      - |github-license|
    * - contribute
      - |github-issues| |github-forks| |github-contributors|
    * - share
      - |share-twitter| |github-stars|

.. |django30x-docs| image:: http://img.shields.io/badge/3.0-docs-0c4b33.svg?style=flat&colorA=8F8F8F
    :target: https://docs.djangoproject.com/en/3.0/
    :alt: Django 3.0 Documentation

.. |help| image:: http://img.shields.io/badge/master-forum-0c4b33.svg?style=flat&colorA=8F8F8F
    :target: https://forum.djangoproject.com/
    :alt: Django Forum

.. |share-twitter| image:: https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmapeveri%2Fdjango-advertising
    :target: https://twitter.com/intent/tweet?text=Download%20and%20use%20%27django-advertising%27%20package%20for%20ads%20management%20with%20Python%20via%20Web%20https://github.com/mapeveri/django-advertising
    :alt: Share at Twitter

.. |github-contributors| image:: https://img.shields.io/github/contributors/mapeveri/django-advertising.svg
    :target: https://github.com/mapeveri/django-advertising/graphs/contributors
    :alt: Github Contributors

.. |github-license| image:: https://img.shields.io/github/license/mapeveri/django-advertising.svg
    :target: https://github.com/mapeveri/django-advertising/blob/master/LICENSE
    :alt: Github License

.. |github-issues| image:: https://img.shields.io/github/issues/mapeveri/django-advertising
    :target: https://github.com/mapeveri/django-advertising/issues
    :alt: Github Issues

.. |github-forks| image:: https://img.shields.io/github/forks/mapeveri/django-advertising
    :target: https://github.com/mapeveri/django-advertising/network/members
    :alt: Github Forks

.. |github-stars| image:: https://img.shields.io/github/stars/mapeveri/django-advertising
    :target: https://github.com/mapeveri/django-advertising/stargazers
    :alt: Github Favorites

.. |python37| image:: https://img.shields.io/badge/Python-3.7-blue
    :target: https://www.python.org/downloads/release/python-375/
    :alt: Python 3.7.5 version

.. |django30x| image:: https://img.shields.io/badge/Django-3.0-blue
    :target: https://github.com/django/django/tree/stable/3.0.x
    :alt: Odoo 13 version

.. |travis| image:: https://travis-ci.org/mapeveri/django-advertising.svg?branch=master
    :target: https://travis-ci.org/mapeveri/django-advertising
    :alt: Travis-CI Build Status

.. |coverall| image:: https://coveralls.io/repos/github/mapeveri/django-advertising/badge.svg?branch=master
    :target: https://coveralls.io/github/mapeveri/django-advertising?branch=master
    :alt: Coveralls Checkout Status

.. end-badges

Django application for show advertising configurable. This application allows you to display advertising in a box (one or many images) and set (Time, url, etc.).


Requirements
------------

- Python 3.7 or higher.

- Django 3.0.8 or higher.


Installing
----------

Install the package using pip:

.. code-block:: console

    pip install django-advertising


Quick start
-----------

1. Add 'advertising.apps.AdvertisingsConfig' to INSTALLED_APPS:

.. code-block:: python

	INSTALLED_APPS = (
        ...
        'advertising.apps.AdvertisingsConfig',
    )

2. Apply migrations:

.. code-block:: console

    python manage.py makemigrations advertising
    python manage.py migrate advertising

3. Add this script in your file .html to use:

.. code-block:: html

	<script src="{% static 'advertising/js/events.js' %}"></script>

4. Add this line in your file .html to use:

.. code-block:: html

	{% load image %}
	{% get_images_advertising height=300 campaign='CMP1' %}


Parameters
----------

1. Height: Min height element size.
2. Campaign: Id unique Advertising Model. (String)


Responsive
----------

If you wish to play with media queries, use the **img-advertising** class.


Example 
-------

It lets do something like that, where a campaign you can add different images and automatically change based on the set time.

.. image:: https://github.com/mapeveri/django-advertising/blob/master/images/example.gif


Contribute
----------

1. Fork this repo and install it

2. Follow PEP8, Style Guide for Python Code

3. Write code

4. Write unit test

5. Send pull request


Contribute
==========

- Issue Tracker: https://github.com/mapeveri/django-advertising/issues
- Source Code: https://github.com/mapeveri/django-advertising


License
=======

- The project is licensed under the BSD License.
