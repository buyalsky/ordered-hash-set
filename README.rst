================
Ordered Hash Set
================

.. image:: https://travis-ci.com/buyalsky/ordered-hash-set.svg?branch=master
    :target: https://travis-ci.com/buyalsky/ordered-hash-set

.. image:: https://badge.fury.io/py/ordered-hash-set.svg
    :target: https://badge.fury.io/py/ordered-hash-set

ordered-hash-set is data structure that stores immutable unique elements.
Unlike built-in set in python, it also keeps the insertion order.

Basic Usage
-----------

.. code-block:: python

  from ordered_hash_set import OrderedSet
  
  s = OrderedSet()

  s.add("London")
  s.add("Tokyo")
  s.add("Paris")
  s.add("Istanbul")
  s.add("London")
  s.remove("Tokyo")

  print(s) # prints: OrderedSet(London, Paris, Istanbul)

Installation
------------

You can easily install via pip:

.. code-block:: console

    pip install ordered-hash-set

