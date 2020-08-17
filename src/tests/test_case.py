import os
import sys

import pytest
from src.ordered_hash_set import OrderedSet

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def filled_set():
    return OrderedSet(1, 2, 3, 4, 5, 6)


class TestBasic:
    def test_contains(self):
        s = filled_set()
        s.add(5)
        assert 5 in s

    def test_remove(self):
        s = OrderedSet()
        s.update(1, 2, 3, 4, 5, "str")
        s.remove(4)
        print(s)
        assert s == OrderedSet(1, 2, 3, 5, "str")
        with pytest.raises(KeyError):
            s.remove(-1)

    def test_remove_first(self):
        s = filled_set()
        s.remove(1)
        assert s[0] == 2
        assert s == OrderedSet(2, 3, 4, 5, 6)

    def test_remove_last(self):
        s = filled_set()
        s.remove(6)
        assert s[-1] == 5

    def test_add_remove_mixed(self):
        s = filled_set()
        s.remove(1)
        assert s[0] == 2
        assert s == OrderedSet(2, 3, 4, 5, 6)
        s.remove(6)
        assert s == OrderedSet(2, 3, 4, 5)
        s.add(7)
        assert s == OrderedSet(2, 3, 4, 5, 7)

    def test_len(self):
        s = OrderedSet()
        s.add(1)
        s.add(1)
        s.add(1)
        s.add(2)
        s.add(3)
        s.remove(1)
        assert len(s) == 2
        assert len(filled_set()) == 6

    def test_len2(self):
        s = OrderedSet()
        s.update(1, 2, 1, 1, 1, 1, 3)
        assert len(s) == 3

    def test_index_access(self):
        s = OrderedSet()
        s.update(1, 2, 3, 4, 5, 6, 7)
        assert s[4] == s[-3] == 5

    def test_equality(self):
        s, s2 = OrderedSet(), OrderedSet()

        s.update(1, 2, 3, 4, 5, 6, 7)
        s2.update(1, 2, 3, 4, 5, 6, 7)

        assert s == s2
        s2.remove(1)
        s2.add(1)
        assert not s == s2

    def test_uniqueness(self):
        s = filled_set()
        s.update(1, 2, 3, 4, 5, 6, 1, 1, 1, 55)
        s.remove(6)
        assert s == OrderedSet(1, 2, 3, 4, 5, 55)

    def test_add_unhashable(self):
        with pytest.raises(TypeError):
            OrderedSet().add([])

    def test_drain(self):
        s = filled_set()
        total = 0
        for num in s.drain():
            total += num
        assert total == 21
        assert s.is_empty()

    def test_drain2(self):
        s = filled_set()
        e = OrderedSet()
        for item in s.drain():
            e.add(item)
        assert s.is_empty()
        assert str(e) == "OrderedSet(1, 2, 3, 4, 5, 6)"

    def test_drain_reversed(self):
        s = filled_set()
        e = OrderedSet()
        for item in s.drain(reverse=True):
            e.add(item)
        assert s.is_empty()
        assert str(e) == "OrderedSet(6, 5, 4, 3, 2, 1)"

    def test_formatting(self):
        assert str(filled_set()) == "OrderedSet(1, 2, 3, 4, 5, 6)"
