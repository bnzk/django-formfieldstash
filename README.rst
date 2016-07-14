django-formfieldstash
*****************

.. image:: https://travis-ci.org/benzkji/django-formfieldstash.svg
    :target: https://travis-ci.org/benzkji/django-formfieldstash

show/hide modelform fields, depending on current value of a dropdown in the form. without page reload.
this is a pure javascript solution, using a modeladminmixin approach.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-formfieldstash

Add ``formfieldstash`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'formfieldstash',
    )

formfieldstash does not need it's own database tables, so no need to migrate.


Usage
------------

Have a look at ``formfieldstash/tests/test_app/admin.py`` for some examples.

.. code-block:: python

    NOPE
    from formfieldstash.admin import assaavdsvad

    class TestModel(models.Model):
        file = FolderlessFileField(blank=True, null=True)


Contribute
------------

Fork and code. Either run `tox` for complete tests, or `python manage.py test --settings=formfieldstash.tests.settings_test`
