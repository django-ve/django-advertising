Django-Advertising
==================

Django application for show advertising configurable. This application allows you to display advertising in a box (one or many images) and set (Time, url, etc.).


Installing
----------

Install the package using pip:

.. code-block:: console

    pip install django-advertising


Quick start
-----------

1. Add 'advertising' to INSTALLED_APPS:

.. code-block:: python

	INSTALLED_APPS = (
        ...
        'advertising',
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
