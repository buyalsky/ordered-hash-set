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
            if next_item:
                self._items[next_item][1][0] = None
        elif item == self._last:
            self._last = previous_item
            if previous_item:
                self._items[previous_item][1][1] = None
        else:
            if previous_item:
                self._items[previous_item][1][1] = next_item
            if next_item:
                self._items[next_item][1][0] = previous_item

    def remove_all(self, *items):
        """
        Removes all given items.
        Raises KeyError if any of the items is not found in the set.

        :param items: (tuple), Items to be removed.
        """
        for item in items:
            self.remove(item)

    def clear(self):
        """
        Clears the set, removing all values.
        """
        self._items.clear()
        self._first = None
        self._last = None

    def drain(self, reverse=False):
        """
        Returns a iterator that removes items from set and yields them.

        :param reverse: If reverse is ``True`` items are yielded from end to start.
        :return: (Iterator), iterator that consumes items.
        """
        if not reverse:
            while self._first:
                item = self._items.pop(self._first)
                yield item[0]
                self._first = item[1][1]
        else:
            while self._last:
                item = self._items.pop(self._last)
                yield item[0]
                self._last = item[1][0]
        self.clear()

    def get_all(self):
        """
        Returns a list containing all items.

        :return: (list), Specified list that contains all items in the set.
        """
        return [_ for _ in self]

    def is_empty(self):
        """
        Determines whether this set is empty or not.

        :return: (bool), ``True`` if this set is empty, ``False`` otherwise.
        """
        return self.__len__() == 0

    def __contains__(self, item):
        return bool(self._items.get(item))

    contains = __contains__

    def contains_all(self, *items):
        """
        Determines whether this set contains all of the items in the specified collection or not.

        :param items: (tuple), the specified items to be searched.
        :return: (bool), ``True`` if all of the items in the specified collection exist in this set, ``False`` otherwise.
        """
        return all(item in self for item in items)

    def contains_any(self, *items):
        """
        Checks whether any of the items exists in this set or not.

        :param items: (tuple), items to be searched.
        :return: (bool), ``True`` if any of the items in the specified collection exist in this set, ``False`` otherwise.
        """
        return any(item in self for item in items)

    def is_disjoint(self, other):
        """
        Returns ``True`` if the set has no elements in common with ``other``.
        Sets(also OrderedSets) are disjoint if and only if their intersection is the empty set.

        :param other: (list | set | OrderedSet), Checked object.
        :return: (bool) If the set has no elements in common with other return True.
        """

        for element in other:
            if element in self:
                return False

        return True

    def is_subset(self, other):
        """
        Tests whether every element in the set is in other.

        :param other: (list | set | OrderedSet), Checked object.
        :return: (bool) If the set is a subset of ``other`` return ``True``.
        """
        
        for element in self:
            if element not in other:
                return False

        return True

    def is_superset(self, other):
        """
        Tests whether every element in other is in the set.

        :param other: (list | set | OrderedSet), Checked object.
        :return: (bool) If the set is the superset of ``other`` return ``True``.
        """
        
        for element in other:
            if element not in self:
                return False

        return True

    def intersection(self, *other):
        """
        Returns a new ordered set with elements common to the set and all others.
        
        :param *other: (list | set | OrderedSet), The sets to check common.
        :return: (OrderedSet) the set with elements common to the OrderedSet object and all ``*other``.
        """
        new_ordered_set = OrderedSet()

        for element in self:
            for obj in other:
                if element not in obj:
                    break
            else:
                new_ordered_set.add(element)

        return new_ordered_set

    def difference(self, *other):
        """
        Returns a new set with elements in the set that are not in the others.

        :param *other: (list | set | OrderedSet), The sets to check difference.
        :return: (OrderedSet) The set of the different elements.
        """
        
        new_ordered_set = OrderedSet()

        for element in self:
            for obj in other:
                if element in obj:
                    break
            else:
                new_ordered_set.add(element)

        return new_ordered_set

    def union(self, *other):
        """
        Returns a new set with elements from the set and all others.

        :param *other: (list | set | OrderedSet), The sets for union.
        :return: (OrderedSet) The new set with elements from the OrderedSet object and all others.
        """
        
        new_ordered_set = OrderedSet()

        for element in self:
            new_ordered_set.add(element)

        for obj in other:
            for element in obj:
                new_ordered_set.add(element)

        return new_ordered_set

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

    def __len__(self):
        return len(self._items)

    def __str__(self):
        items = tuple(i for i in self)
        return "OrderedSet("+', '.join(['{}']*(len(items))).format(*items) + ")"

    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            return False

        return self._items == other._items
