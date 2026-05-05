import unittest
from library import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def test_details(self):
        item = LibraryItem("1984", "George Orwell", 1949)
        self.assertEqual(item.details(), "1984 - George Orwell (1949)")

        item2 = LibraryItem("Python", "Guido van Rossum", 1991)
        self.assertEqual(item2.details(), "Python - Guido van Rossum (1991)")

if __name__ == "__main__":
    unittest.main()