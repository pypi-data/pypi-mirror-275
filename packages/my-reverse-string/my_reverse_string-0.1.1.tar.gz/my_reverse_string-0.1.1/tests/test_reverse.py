# tests/test_reverse.py

import unittest
from reverse_string003 import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

if __name__ == "__main__":
    unittest.main()
