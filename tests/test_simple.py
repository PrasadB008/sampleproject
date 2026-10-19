# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one, clamp


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)


class TestClamp(unittest.TestCase):

    def test_clamp_value_within_range(self):
        """Test that value within range is returned unchanged."""
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_clamp_value_below_low(self):
        """Test that value below low is clamped to low."""
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_clamp_value_above_high(self):
        """Test that value above high is clamped to high."""
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_clamp_value_equals_low(self):
        """Test that value equal to low is returned unchanged."""
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_clamp_value_equals_high(self):
        """Test that value equal to high is returned unchanged."""
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_low_equals_high(self):
        """Test that clamping works when low equals high."""
        self.assertEqual(clamp(5, 10, 10), 10)
        self.assertEqual(clamp(15, 10, 10), 10)

    def test_clamp_low_greater_than_high_raises_error(self):
        """Test that ValueError is raised when low > high."""
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)

    def test_clamp_with_floats(self):
        """Test that clamp works with float values."""
        self.assertEqual(clamp(5.5, 0.0, 10.0), 5.5)
        self.assertEqual(clamp(-5.5, 0.0, 10.0), 0.0)
        self.assertEqual(clamp(15.5, 0.0, 10.0), 10.0)


if __name__ == '__main__':
    unittest.main()
