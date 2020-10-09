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
    
Or install from source:

.. code-block:: console

    python3 setup.py install

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

  # Thanks to the hashing. Time complexity of checking
  # if an element present in a collection is O(1).
  # Which is faster than regular list: O(n).
  if "Paris" in s:
    print("Paris is in the set.")

  # It is also possible, but not recommended due to inefficiency,
  # to get the item by index:
  assert s[2] == "Istanbul"


API Documentation
-----------------

Please see `API Reference Page <https://buyalsky.github.io/ordered-hash-set/en/master/rst/ordered_hash_set.html>`_

