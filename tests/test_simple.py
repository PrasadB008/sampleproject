# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one, clamp


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_clamp_value_within_range(self):
        """Test clamp returns value when it's within range"""
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_clamp_value_below_range(self):
        """Test clamp returns low when value is below range"""
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_clamp_value_above_range(self):
        """Test clamp returns high when value is above range"""
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_clamp_value_at_low_boundary(self):
        """Test clamp returns low when value equals low"""
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_clamp_value_at_high_boundary(self):
        """Test clamp returns high when value equals high"""
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_low_equals_high(self):
        """Test clamp when low equals high"""
        self.assertEqual(clamp(5, 5, 5), 5)

    def test_clamp_low_greater_than_high_raises_error(self):
        """Test clamp raises ValueError when low > high"""
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)

    def test_clamp_with_floats(self):
        """Test clamp works with float values"""
        self.assertEqual(clamp(5.5, 0.0, 10.0), 5.5)
        self.assertEqual(clamp(-5.5, 0.0, 10.0), 0.0)
        self.assertEqual(clamp(15.5, 0.0, 10.0), 10.0)


if __name__ == '__main__':
    unittest.main()
