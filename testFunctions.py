import unittest
from tictactoeFuncs import *


class TestCases(unittest.TestCase):
    def test_checkRows(self):
        self.assertEqual(checkRows(['X', 'X', 'X', " ", " ", " ", " ", 'O', 'O']), (True, 'X'))
        self.assertEqual(checkRows([' ', 'X', 'X', " ", " ", " ", "O", 'O', 'O']), (True, 'O'))

    def test_checkCols(self):
        self.assertEqual(checkCols(['X', 'X', 'X', " ", " ", " ", " ", 'O', 'O']), (False, 'X'))
        self.assertEqual(checkCols(['X', 'O', 'X', "X", " ", " ", "X", 'O', 'O']), (True, 'X'))

    def test_checkDiags(self):
        self.assertEqual(checkDiags(['X', 'O', 'O', " ", "O", " ", "O", 'O', 'O']), (True, 'O'))
        self.assertEqual(checkDiags(['X', 'O', 'X', "X", " ", " ", "X", 'O', 'O']), (False, 'X'))

    def test_boardFull(self):
        self.assertEqual(boardFull(['X', 'O', 'X', "X", " ", " ", "X", 'O', 'O']), (False))
        self.assertEqual(boardFull(['X', 'O', 'X', "X", "X", "O", "X", 'O', 'O']), (True))

    def test_checkWin(self):
        self.assertEqual(checkWin(['X', 'O', 'X', "X", " ", " ", "X", 'O', 'O']), (True))
        self.assertEqual(checkWin(['X', 'O', 'X', "X", " ", " ", " ", 'O', 'O']), (False))



if __name__ == '__main__':
    unittest.main()
