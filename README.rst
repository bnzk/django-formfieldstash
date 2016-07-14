django-formfieldstash
*****************

.. image:: https://travis-ci.org/benzkji/django-formfieldstash.svg
    :target: https://travis-ci.org/benzkji/django-formfieldstash

show/hide modelform fields, based on current value of a dropdown in the same field.


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

    from formfieldstash.admin import assaavdsvad

    class TestModel(models.Model):
        file = FolderlessFileField(blank=True, null=True)


Contribute
------------

Fork and code. Either run `tox` for complete tests, or `python manage.py test --settings=folderless.tests.settings_test`


Credits / Idea
--------------

main repository: https://github.com/benzkji/django-folderless . many similiar things already exist. no wonder this project is heavily experienced by https://github.com/stefanfoulis/django-filer, and to some extent, feincms.module.medialibrary and https://github.com/samluescher/django-media-tree. initial idea credits: https://github.com/wullerot/ (manipulated django-filer to hide folders completely). more ideas: http://de.slideshare.net/motivesystems/slideshare-upload-gartner-pcc-presentation-going-folderless-with-metadata

this project uses http://semver.org.
