# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one, clamp


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_clamp_value_within_range(self):
        """Test that clamp returns the value when it's within the range."""
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_clamp_value_below_range(self):
        """Test that clamp returns low when value is below the range."""
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_clamp_value_above_range(self):
        """Test that clamp returns high when value is above the range."""
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_clamp_value_at_low_boundary(self):
        """Test that clamp returns low when value equals low."""
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_clamp_value_at_high_boundary(self):
        """Test that clamp returns high when value equals high."""
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_low_equals_high(self):
        """Test that clamp works when low equals high."""
        self.assertEqual(clamp(5, 10, 10), 10)
        self.assertEqual(clamp(15, 10, 10), 10)

    def test_clamp_with_negative_numbers(self):
        """Test that clamp works with negative numbers."""
        self.assertEqual(clamp(-5, -10, -1), -5)
        self.assertEqual(clamp(-15, -10, -1), -10)
        self.assertEqual(clamp(0, -10, -1), -1)

    def test_clamp_with_floats(self):
        """Test that clamp works with floating point numbers."""
        self.assertEqual(clamp(5.5, 0.0, 10.0), 5.5)
        self.assertEqual(clamp(-5.5, 0.0, 10.0), 0.0)
        self.assertEqual(clamp(15.5, 0.0, 10.0), 10.0)

    def test_clamp_raises_error_when_low_greater_than_high(self):
        """Test that clamp raises ValueError when low > high."""
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == '__main__':
    unittest.main()
