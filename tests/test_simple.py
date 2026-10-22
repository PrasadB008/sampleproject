# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

import pytest

from sample.simple import add_one, multiply


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)


@pytest.mark.parametrize(
    "a, b, expected",
    [(3, 4, 12), (0, 5, 0), (-2, 3, -6), (-2, -3, 6), (1.5, 2, 3.0)],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


if __name__ == '__main__':
    unittest.main()
