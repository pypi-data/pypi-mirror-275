import sys
import os

import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from json_dict_diff import diff, ValidationException


class A:
    pass


@pytest.mark.parametrize(
    "a,b",
    [
        (A(), 1),
        (1, A()),
        (1, {"a": A()}),
        ({"a": A()}, 1),
        (1, [A()]),
        ([A()], 1),
        (1, (A())),
        ((A()), 1),
    ],
)
def test_validation_exception(a, b):
    with pytest.raises(ValidationException):
        diff(a, b)


@pytest.mark.parametrize(
    "a,b",
    [
        ("a", "a"),
        (1, 1),
        (1.0, 1.0),
        (True, True),
        (False, False),
        ({}, {}),
        ([], []),
        ((), ()),
        (set(), set()),
        (None, None),
    ],
)
def test_simple_equal(a, b):
    assert diff(a, b) is None


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("a", "b", ("a", "b")),
        (1, 2, (1, 2)),
        (1.0, 2.0, (1.0, 2.0)),
        (True, False, (True, False)),
        (False, True, (False, True)),
        ({}, [], ({}, [])),
        ([], {}, ([], {})),
        ((), {}, ((), {})),
        (set(), {}, (set(), {})),
        (None, 1, (None, 1)),
    ],
)
def test_simple_unequal(a, b, expected):
    assert diff(a, b) == expected


@pytest.mark.parametrize(
    "a,b",
    [
        ({"a": 1}, {"a": 1}),
        ({"a": 1, "b": {"c": True}}, {"a": 1, "b": {"c": True}}),
        # order in lists should not matter
        ({"a": 1, "b": {"c": [3, 2, 4, 1]}}, {"a": 1, "b": {"c": [1, 4, 3, 2]}}),
        # multiple identical elements in lists should not matter
        (
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
        ),
        (
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [2, 1]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
        ),
        (
            {"a": 1, "b": {"c": [[{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [2, 1]}]]}},
            {"a": 1, "b": {"c": [[{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]]}},
        ),
        # also for tuples
        (
            {"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [2, 1]})}},
            {"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]})}},
        ),
        # and sets
        (set((1, 2)), set((1, 2))),
        # should also work if wrapped in a list
        (
            [{"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [2, 1]})}}],
            [{"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]})}}],
        ),
    ],
)
def test_equal(a, b):
    assert diff(a, b) is None


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ({"a": 1}, {"a": 2}, ({"a": (1, 2)})),
        ({"a": 1, "b": {"c": True}}, {"a": 1, "b": {"c": False}}, {"b": {"c": (True, False)}}),
        ({"a": 1, "b": {"c": True}}, {"a": 2, "b": {"c": False}}, {"a": (1, 2), "b": {"c": (True, False)}}),
        # order in lists should not matter (inserting/deleting/updating elements)
        ({"a": 1, "b": {"c": [3, 2, 4, 1]}}, {"a": 1, "b": {"c": [1, 4, 3, 2, 8]}}, {"b": {"c": [(None, 8)]}}),
        ({"a": 1, "b": {"c": [3, 2, 4, 1]}}, {"a": 1, "b": {"c": [4, 3, 2]}}, {"b": {"c": [(1, None)]}}),
        ({"a": 1, "b": {"c": [3, 2, 4, 1]}}, {"a": 1, "b": {"c": [4, 8, 3, 2]}}, {"b": {"c": [(1, 8)]}}),
        # if values of the same types are substituted, the substition should still be deterministic
        (
            {"a": 1, "b": {"c": [True, 2, 4, 1]}},
            {"a": 1, "b": {"c": [4, 8, False, 2]}},
            {"b": {"c": [(True, False), (1, 8)]}},
        ),
        (
            {"a": 1, "b": {"c": [3, False, 4, 1, True]}},
            {"a": 1, "b": {"c": [4, True, 8, 3, True]}},
            {"b": {"c": [(False, True), (1, 8)]}},
        ),
        # multiple identical elements in lists should not matter
        (
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"b": {"c": [{"x": [(2, None)]}]}},
        ),
        (
            {"a": 1, "b": {"c": [{"d": 1, "x": [1]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"b": {"c": [{"x": [(None, 2)]}]}},
        ),
        (
            {"a": 1, "b": {"c": [{"d": 2, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [2, 1]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"b": {"c": [{"d": (2, 1)}]}},
        ),
        (
            {"a": 1, "b": {"c": [{"d": 2, "x": [1]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"a": 1, "b": {"c": [{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]}},
            {"b": {"c": [{"d": (2, 1), "x": [(None, 2)]}]}},
        ),
        (
            {"a": 1, "b": {"c": [[{"d": 2, "x": [1]}, {"e": False, "x": 1}, {"d": 1, "x": [2, 1]}]]}},
            {"a": 1, "b": {"c": [[{"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]}]]}},
            {"b": {"c": [[{"d": (2, 1), "x": [(None, 2)]}, {"e": (False, 1), "x": (1, True)}]]}},
        ),
        # also for tuples
        (
            {"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": [1, 2], "x": True}, {"d": 1, "x": [2, 1]})}},
            {"a": 1, "b": {"c": ({"d": 1, "x": [1, 2]}, {"e": 1, "x": True}, {"d": 1, "x": [1, 2]})}},
            {"b": {"c": [{"e": ([1, 2], 1)}]}},
        ),
        # and sets (be aware that set considers e.g. 1 and True to be equal)
        (set((2, 3)), set((2, True)), [(3, True)]),
    ],
)
def test_unequal(a, b, expected):
    assert diff(a, b) == expected
