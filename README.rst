================
Ordered Hash Set
================

ordered-hash-set is data structure that stores immutable unique elements.
Unlike built-in set in python, it is also keeps the insertion order.

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
You can easily install via pip:

.. code-block:: console

    pip install ordered-hash-set

