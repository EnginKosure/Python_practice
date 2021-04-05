import unittest

from fzlt139 import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

    @unittest.skip("WIP")
    def test_is_consistent(self):
        phonebook = PhoneBook()
        self.assertTrue(phonebook.is_consistent())
