from unittest import TestCase
from fetchData import fetchData

class testdata(TestCase):
    def test_fetch(self):
        f = fetchData()

        expected = ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars', 'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi']

        self.assertListEqual(f.data(),expected)