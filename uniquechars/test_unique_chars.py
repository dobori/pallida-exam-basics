import unittest
from unique_chars import unique_characters

class TestUniqueCharacters(unittest.TestCase):

    def test_all_unique_chars(self):
        self.assertEqual(unique_characters("elmegyek"), ['l', 'm', 'g', 'y', 'k'])

    def test_none_type(self):
        self.assertEqual(unique_characters(None), 0)

    def test_number_input(self):
        self.assertFalse(unique_characters(2))

if __name__ == '__main__':
    unittest.main()