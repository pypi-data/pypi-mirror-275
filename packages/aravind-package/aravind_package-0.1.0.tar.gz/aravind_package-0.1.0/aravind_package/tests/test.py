import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from aravind_package.package import reverse_string, to_uppercase, count_vowels
import unittest

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("HeLLo"), "HELLO")
        self.assertEqual(to_uppercase(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("xyz"), 0)

if __name__ == '__main__':
    unittest.main()
