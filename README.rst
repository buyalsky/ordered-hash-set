================
Ordered Hash Set
================

.. image:: https://travis-ci.com/buyalsky/ordered-hash-set.svg?branch=master
    :target: https://travis-ci.com/buyalsky/ordered-hash-set

.. image:: https://img.shields.io/pypi/v/ordered-hash-set
    :alt: PyPI
    :target: https://pypi.org/project/ordered-hash-set/

ordered-hash-set is data structure that stores immutable unique elements.
Unlike built-in set in python, it also keeps the insertion order.

Installation
------------

Install via ``pip``:

.. code-block:: console

    pip install ordered-hash-set

Basic Usage
-----------

.. code-block:: python

  from ordered_hash_set import OrderedSet
  
  s = OrderedSet()

  s.add("London")
  s.add("Tokyo")
  # you can add multiple entries at once, like this:
  s.update("Paris", "Istanbul")
  s.add("London")
  s.remove("Tokyo")

  print(s) # prints: OrderedSet(London, Paris, Istanbul)

API Documentation
-----------------

Please see `API Reference <https://buyalsky.github.io/ordered-hash-set/en/master/rst/ordered_hash_set.html>`_ for more info

