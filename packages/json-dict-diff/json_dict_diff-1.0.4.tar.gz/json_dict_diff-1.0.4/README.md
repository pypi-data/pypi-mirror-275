# Json Dict Diff

Library for creating a minimal diff of two json-compatible Python dictionaries.

This library can be used to compare two json-compatible Python dictionaries (i.e. dictionaries, lists, ... containing only the following primitives: `int`, `float`, `str`, `list`, `dict`, `set`, `tuple`, `bool`) and generates a "minimal" diff.
The diff is represented as a dictionary where insertions/deletions/substitutions are represented as tuples.
For example the following two dictionaries:

```py
diff(
  { "a": [ { "b": 1, "c": True }, 1.0, "x" ], "d": 1 },
  { "a": [ { "b": 2, "c": True }, 1.0, "y", True ] }
)
```

will result in the following diff:

```py
{ "a": [ { "b": (1, 2) }, ("x", "y"), (None, True) ], "d": (1, None) }
```

Here the tuples `(1, 2), ("x", "y"), (None, True), (1, None)` represent the substitions that happened.
`None` implies that an object was either removed or added.

If there is no diff (e.g.: `diff({ "a": 1 }, { "a": 1 })`) the result will be `None`. In this sense,
the library can also be used to compare two json-compatible dictionaries.

---

If an object of any other type is used in a dict, list, ..., a `ValidationException` will be raised.

## Exports

```py
JDict = Union[int, float, str, List["Result"], Dict[str, "Result"], Tuple["Result"], Set["Result"], None]

class ValidationException

def validate(a: JDict):

def diff(a: JDict, b: JDict) -> JDict:
```

## Notes

Primitive objects such as ints, floats, ... can also be diffed which will result in a single tuple of a substition.
For example:

```py
diff("a", "b") == ("a", "b")
diff("a", "a") is None
```

---

The diff will treat lists, sets and tuples as lists, which means that the result will contain lists instead of sets or tuples.
This is due to tuples being reserved for the substitution results.

---

If it is not clear which element in a list might be substituted this library makes no guarantees on the actual substitution.
For example:

```py
diff([1, 2, 3], [1, 4, 5])
```

can result either in: `[ (2, 4), (3, 5) ]` or `[ (3, 4), (2, 5) ]`.

---

`None` elements might or might not show up as a diff.
For example:

```py
diff([ None, 1 ], [1])
```

might result in `[ (None, 1) ]` or `None` (i.e. no diff).
