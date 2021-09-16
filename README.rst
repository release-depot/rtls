========================
Real Time Locator System
========================


.. image:: https://img.shields.io/pypi/v/rtls.svg
        :target: https://pypi.python.org/pypi/rtls

.. image:: https://readthedocs.org/projects/rtls/badge/?version=latest
        :target: https://rtls.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/release-depot/rtls/shield.svg
     :target: https://pyup.io/repos/github/release-depot/rtls/
     :alt: Updates


RTLS, or Real Time Locator System, is an abstraction layer for tracking changes to code through their lifecycle


* Free software: MIT license
* Documentation: https://rtls.readthedocs.io.

API
---

Test call - /rtls/[package]/[changeId] (GET)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test call::

    $ curl localhost:8080/rtls/mypackage/I123456
    {"msg": "Test with mypackage"}

Development
-----------

See **CONTRIBUTING.rst**.

Container image creation
~~~~~~~~~~~~~~~~~~~~~~~~

Building the container image::

    $ pipenv shell
    $ ansible-bender build ./build.yml

Running the container image::

    $ podman run -d --name rtls -p 8080:80 localhost/rtls:latest

Reading the container logs::

    $ podman logs rtls
    $ podman exec -it rtls cat /var/log/nginx/error.log | less


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
