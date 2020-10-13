import os
import sys

import pytest
from src.ordered_hash_set import OrderedSet

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@pytest.fixture
def filled_set():
    return OrderedSet(1, 2, 3, 4, 5, 6)


def test_contains(filled_set):
    filled_set.add(5)
    assert 5 in filled_set


def test_contains_any(filled_set):
    assert filled_set.contains_any(7, 8, 4, 9, "str")
    assert not filled_set.contains_any(7, "str", 5.5)


def test_contains_all(filled_set):
    assert filled_set.contains_all(1, 2, 3, 4, 5)
    assert not filled_set.contains_all(1, 2, 3, 4, 5, 5.5)


def test_remove(filled_set):
    filled_set.update(1, 2, 3, 4, 5, "str")
    filled_set.remove_all(4, 6)
    print(filled_set)
    assert filled_set == OrderedSet(1, 2, 3, 5, "str")
    with pytest.raises(KeyError):
        filled_set.remove(-1)


def test_remove_first(filled_set):
    filled_set.remove(1)
    assert filled_set[0] == 2
    assert filled_set == OrderedSet(2, 3, 4, 5, 6)


def test_remove_last(filled_set):
    filled_set.remove(6)
    assert filled_set[-1] == 5


def test_add_remove_mixed(filled_set):
    filled_set.remove(1)
    assert filled_set[0] == 2
    assert filled_set == OrderedSet(2, 3, 4, 5, 6)
    filled_set.remove(6)
    assert filled_set == OrderedSet(2, 3, 4, 5)
    filled_set.add(7)
    assert filled_set == OrderedSet(2, 3, 4, 5, 7)


def test_len(filled_set):
    s = OrderedSet()
    s.add(1)
    s.add(1)
    s.add(1)
    s.add(2)
    s.add(3)
    s.remove(1)
    assert len(s) == 2
    assert len(filled_set) == 6


def test_len2():
    s = OrderedSet()
    s.update(1, 2, 1, 1, 1, 1, 3)
    assert len(s) == 3


def test_index_access():
    s = OrderedSet()
    s.update(1, 2, 3, 4, 5, 6, 7)
    assert s[4] == s[-3] == 5


def test_equality():
    s, s2 = OrderedSet(), OrderedSet()

    s.update(1, 2, 3, 4, 5, 6, 7)
    s2.update(1, 2, 3, 4, 5, 6, 7)

    assert s == s2
    s2.remove(1)
    s2.add(1)
    assert not s == s2


def test_uniqueness(filled_set):
    filled_set.update(1, 2, 3, 4, 5, 6, 1, 1, 1, 55)
    filled_set.remove(6)
    assert filled_set == OrderedSet(1, 2, 3, 4, 5, 55)


def test_add_unhashable():
    with pytest.raises(TypeError):
        OrderedSet().add([])


def test_drain(filled_set):
    total = 0
    for num in filled_set.drain():
        total += num
    assert total == 21
    assert filled_set.is_empty()


def test_drain2(filled_set):
    e = OrderedSet()
    for item in filled_set.drain():
        e.add(item)
    assert filled_set.is_empty()
    assert str(e) == "OrderedSet(1, 2, 3, 4, 5, 6)"


def test_drain_reversed(filled_set):
    e = OrderedSet()
    for item in filled_set.drain(reverse=True):
        e.add(item)
    assert filled_set.is_empty()
    assert str(e) == "OrderedSet(6, 5, 4, 3, 2, 1)"


def test_formatting(filled_set):
    assert str(filled_set) == "OrderedSet(1, 2, 3, 4, 5, 6)"


def test_is_disjoint(filled_set):
    other_parameter = OrderedSet(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    example = OrderedSet()
    for parm in other_parameter:
        example.add(parm)
        assert not filled_set.is_disjoint(example)
    example.clear()
    other_parameter.remove_all(1, 2, 3, 4, 5, 6)
    for parm in other_parameter:
        example.add(parm)
        assert filled_set.is_disjoint(example)


def test_is_subset(filled_set):
    other_parameter = OrderedSet(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    example = OrderedSet()
    for parm in other_parameter:
        example.add(parm)
        if parm <= 5:
            assert not filled_set.is_subset(example)
        else:
            assert filled_set.is_subset(example)


def test_is_superset(filled_set):
    other_parameter = OrderedSet(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    example = OrderedSet()
    for parm in other_parameter:
        example.add(parm)
        if parm <= 6:
            assert filled_set.is_superset(example)
        else:
            assert not filled_set.is_superset(example)


def test_intersection(filled_set):
    assert str(
        filled_set.intersection({1, 2, 3}, OrderedSet(1, 2, 3, 4), OrderedSet(3, 1, 5), [1, 2, 3, 4, 5, 6])
    ) == "OrderedSet(1, 3)"
    assert str(
        filled_set.intersection(OrderedSet(1, 2, 3, 4), [7, 5, 6], {3, 2, 1}, {}, filled_set)
    ) == "OrderedSet()"


def test_difference(filled_set):
    assert str(
        filled_set.difference({6, 7, 8}, OrderedSet(5, 4, 7, 0), OrderedSet(5, 4, 7, 9), {})
    ) == "OrderedSet(1, 2, 3)"
    assert str(
        filled_set.difference(OrderedSet(1, 2, 3), {}, OrderedSet(), filled_set)
    ) == "OrderedSet()"


def test_union(filled_set):
    assert str(
        filled_set.union([7, 8, 9], {1, 2, 3}, (5, 2, 9,), OrderedSet(), OrderedSet(10), filled_set)
    ) == "OrderedSet(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
