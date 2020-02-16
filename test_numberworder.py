import unittest
from NumberWorder import Convert_To_Word


class TestNumberWorder(unittest.TestCase):
    def test_convert(self):
        # Test convert when input is number
        # and greater than 0
        self.assertAlmostEqual(Convert_To_Word("1"), "one ")
        self.assertAlmostEqual(Convert_To_Word("234"), "two three four ")
        self.assertAlmostEqual(Convert_To_Word(
            "-3"), "Input cannot be negative")
        self.assertAlmostEqual(Convert_To_Word(
            "string"), "Input is not a number")
        self.assertAlmostEqual(Convert_To_Word(""), "Input cannot be empty")
