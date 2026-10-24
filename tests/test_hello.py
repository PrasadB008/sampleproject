import contextlib
import io
import unittest

from sample.hello import main


class TestHello(unittest.TestCase):

    def test_main_prints_greeting(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            main()
        self.assertEqual(buffer.getvalue(), "Hello from sample\n")


if __name__ == '__main__':
    unittest.main()
