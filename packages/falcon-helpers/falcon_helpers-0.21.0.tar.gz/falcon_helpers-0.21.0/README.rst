.. default-role:: code
.. role:: python(code)
  :language: python


.. image:: https://codecov.io/gl/skosh/falcon-helpers/branch/master/graph/badge.svg
  :target: https://codecov.io/gl/skosh/falcon-helpers

.. image:: https://gitlab.com/skosh/falcon-helpers/badges/master/pipeline.svg
  :target: https://gitlab.com/skosh/falcon-helpers/commits/master


==============
Falcon Helpers
==============

A number of helpful utilities to make working with Falcon Framework a breeze.


Quickstart
----------

.. code:: sh

  $ pip install falcon-helpers


.. code::

  import falcon
  import falcon_helpers

  api = falcon.App(
    middlewares=[
      falcon_helpers.middlewares.StaticsMiddleware()
    ]
  )


Development
-----------
1. Create a Python 3.10 virtual environment, and activate it.
2. ``pip install -e .[dev]``
3. ``pytest`` or  run ``tox`` and verify the tests pass.
