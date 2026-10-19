# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one, clamp


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_clamp_value_within_range(self):
        """Test clamp returns value when it's within [low, high]"""
        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_value_below_low(self):
        """Test clamp returns low when value is below low"""
        self.assertEqual(clamp(-5, 0, 10), 0)
        self.assertEqual(clamp(-100, -50, 50), -50)

    def test_clamp_value_above_high(self):
        """Test clamp returns high when value is above high"""
        self.assertEqual(clamp(15, 0, 10), 10)
        self.assertEqual(clamp(100, -50, 50), 50)

    def test_clamp_with_negative_range(self):
        """Test clamp works with negative ranges"""
        self.assertEqual(clamp(-25, -50, -10), -25)
        self.assertEqual(clamp(-60, -50, -10), -50)
        self.assertEqual(clamp(-5, -50, -10), -10)

    def test_clamp_with_floats(self):
        """Test clamp works with floating point numbers"""
        self.assertEqual(clamp(5.5, 0.0, 10.0), 5.5)
        self.assertEqual(clamp(-5.5, 0.0, 10.0), 0.0)
        self.assertEqual(clamp(15.5, 0.0, 10.0), 10.0)

    def test_clamp_low_equals_high(self):
        """Test clamp when low equals high"""
        self.assertEqual(clamp(5, 10, 10), 10)
        self.assertEqual(clamp(15, 10, 10), 10)
        self.assertEqual(clamp(10, 10, 10), 10)

    def test_clamp_raises_error_when_low_greater_than_high(self):
        """Test clamp raises ValueError when low > high"""
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)
        with self.assertRaises(ValueError):
            clamp(5, 100, -100)


if __name__ == '__main__':
    unittest.main()
