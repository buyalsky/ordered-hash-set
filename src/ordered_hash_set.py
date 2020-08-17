class OrderedSet:
    def __init__(self, *items):
        self._items = {}
        self._first = None
        self._last = None
        if items:
            self.update(*items)

    def add(self, item):
        """
        Adds the item to set if it is not exist.
        Raises TypeError if specified item is not hashable

        :param item: (object), item to be added.
        """
        if not self._first:
            self._first = item

        if item not in self._items.keys():
            self._items[item] = item, [self._last, None]
            if len(self._items) != 1:
                self._items[self._last][1][1] = item
            self._last = item

    def update(self, *items):
        """
        Adds multiple items at once.
        Raises TypeError, if any of these items are not hashable,

        :param items: (object), items, which must have ``__hash__`` method, to be inserted.
        """
        for item in items:
            self.add(item)

    def remove(self, item):
        """
        Removes given item from set.
        Raises KeyError if item is not found.

        :param item: (object), Removed item
        """
        removed_item = self._items.pop(item)
        previous_item, next_item = removed_item[1]
        if item == self._first:
            self._first = next_item
            self._items[next_item][1][0] = None
        elif item == self._last:
            self._last = previous_item
            self._items[previous_item][1][1] = None
        else:
            self._items[previous_item][1][1] = next_item
            self._items[next_item][1][0] = previous_item

    def remove_all(self, *items):
        for item in items:
            self.remove(item)

    def clear(self):
        """
        Clears the set.
        """
        self._items.clear()
        self._first = None
        self._last = None

    def get_all(self):
        return list(_ for _ in self)

    def is_empty(self):
        """
        Determines whether this set is empty or not.

        :return: (bool), ``True`` if this set is empty, ``False`` otherwise.
        """
        return self.__len__() == 0

    def __getitem__(self, index):
        if index < 0:
            return tuple(i for i in self)[index]

        if self.__len__() >= index:
            IndexError("Index is out of range")

        item = self._first

        for i in range(index):
            item = self._items[self._items[item][1][1]][0]

        return item

    def __iter__(self):
        self._next = self._first
        return self

    def __next__(self):
        item = self._next
        if not item:
            raise StopIteration
        self._next = self._items[self._next][1][1]
        return item

    def __contains__(self, item):
        return bool(self._items.get(item))

    def contains_all(self, *items):
        """
        Determines whether this set contains all of the items in the specified collection or not.

        :param items: (tuple), the specified items to be searched.
        :return: (bool), ``True`` if all of the items in the specified collection exist in this set, ``False`` otherwise.
        """
        return all(self.contains(item) for item in items)

    def contains_any(self, *items):
        """
        Checks whether any of the items exists in this set or not.

        :param items: (tuple), items to be searched.
        :return: (bool), ``True`` if any of the items in the specified collection exist in this set, ``False`` otherwise.
        """
        return any(self.contains(item) for item in items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "OrderedSet("+', '.join(['{}']*self.__len__()).format(*(i for i in self)) + ")"

    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            return False

        return self._items == other._items

    contains = __contains__
