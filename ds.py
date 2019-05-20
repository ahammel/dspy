"""Disjoint set data structure implementation

"""

from collections import namedtuple
from itertools import groupby


class MutableDisjointSet(object):
    """DisjointSet where add_set mutates the object.

    """

    def __init__(self, *elems):
        self._dict = {}
        for elem in elems:
            self._add(elem)

    def __eq__(self, other):
        other_segments = getattr(other, "segments", None)
        return callable(other_segments) and self.segments() == other_segments()

    def __repr__(self):
        set_strings = []
        for s in self.segments():
            string = "{{{}}}".format(", ".join(str(elem) for elem in s))
            set_strings.append(string)

        return "disjoint({})".format(", ".join(set_strings))

    def add_set(self, first, *rest):
        self._add(first)
        for elem in rest:
            self._add(elem)
            self._union(first, elem)
        return self

    def elems(self):
        return frozenset(self._dict.keys())

    def segments(self):
        keys = sorted(self._dict.keys(), key=self._root)
        return frozenset([
            frozenset(values)
            for _, values
            in groupby(keys, key=self._root)])

    def _add(self, elem):
        if elem not in self._dict:
            self._dict[elem] = {"parent": elem, "size": 1}

    def _root(self, elem):
        if elem != self._dict[elem]["parent"]:
            self._dict[elem]["parent"] = self._root(self._dict[elem]["parent"])
        return self._dict[elem]["parent"]

    def _union(self, x, y):
        x_root = self._root(x)
        y_root = self._root(y)

        if x_root == y_root:
            return

        lesser_root, greater_root = (
            (x_root, y_root)
            if self._dict[x_root]["size"] < self._dict[y_root]["size"]
            else (y_root, x_root)
        )
        self._dict[lesser_root]["parent"] = greater_root
        self._dict[greater_root]["size"] += self._dict[lesser_root]["size"]
