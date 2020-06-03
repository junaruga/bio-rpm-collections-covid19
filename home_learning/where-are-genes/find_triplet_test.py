import find_triplet as ft
import unittest

class TestRetrieveTripletPosition(unittest.TestCase):
    def test_seek_orf_exact_match(self):
        self.assertEqual([0],
                         ft.retrieve_triplet_position("ATG", "ATG"),
                         )
    def test_seek_orf_exact_multiple_match(self):
        self.assertEqual([0, 6],
                         ft.retrieve_triplet_position("ATGATCATGG", "ATG"),
                         )
    def test_seek_orf_no_match(self):
        self.assertEqual([],
                         ft.retrieve_triplet_position("GTA", "ATG"),
                         )
    def test_seek_orf_non_triplet(self):
        with self.assertRaises(ValueError):
            ft.retrieve_triplet_position("GTA", "GA")

unittest.main(argv=[""], verbosity=2, exit=False)
