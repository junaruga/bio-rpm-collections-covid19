import unittest

import find_orf as fo


class TestSeekOrf(unittest.TestCase):
    def test_seek_orf(self):
        self.assertEqual(fo.seek_orf([5, 100, 1000, 3000], [0, 800, 2000]),
                         [(5, 800), (100, 800), (1000, 2000)])


unittest.main(argv=[''], verbosity=3, exit=False)
