from .context import ds


def test_empty_disjoint_set_has_no_elems():
    assert ds.MutableDisjointSet().elems() == set()


def test_empty_disjoint_set_has_no_sets():
    assert ds.MutableDisjointSet().sets() == set()


def test_singleton_disjoint_set_has_one_elem():
    assert ds.MutableDisjointSet(1).elems() == set([1])


def test_singleton_disjoint_set_has_one_a_singleton_set():
    actual = ds.MutableDisjointSet(1).sets()
    expected = frozenset([frozenset([1])])
    assert actual == expected


def test_disjoint_set_with_a_union():
    actual = ds.MutableDisjointSet(1, 2, 3)\
        .add_set(1, 2)\
        .sets()
    expected = frozenset([
        frozenset([1, 2]),
        frozenset([3]),
    ])
    assert actual == expected


def test_transitivity():
    first = ds.MutableDisjointSet(1, 2, 3, 4)\
        .add_set(1, 2)\
        .add_set(2, 3)
    second = ds.MutableDisjointSet(1, 2, 3, 4)\
        .add_set(2, 3)\
        .add_set(1, 2)
    assert first == second


def test_adding_the_same_set_twice_is_a_no_op():
    first = ds.MutableDisjointSet()\
        .add_set(1, 2)
    second = ds.MutableDisjointSet()\
        .add_set(1, 2)\
        .add_set(1, 2)
    assert first == second


def test_repr_singleton():
    assert repr(ds.MutableDisjointSet(1)) == "disjoint({1})"

# Mutation testing results


def test_disjoint_sets_are_not_equal_to_regular_sets():
    assert ds.MutableDisjointSet(1) != set([1])


def test_repr_two_sets():
    assert repr(ds.MutableDisjointSet(1, 2)) in [
        "disjoint({1}, {2})", "disjoint({2}, {1})"]


def test_repr_set_of_two():
    assert repr(ds.MutableDisjointSet().add_set(1, 2)) in [
        "disjoint({1, 2})", "disjoint({2, 1})"]
