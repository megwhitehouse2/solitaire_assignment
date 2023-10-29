
import unittest
from board import *

class TestBoard(unittest.TestCase):
    
    def test_initial_board(self):
        board = Board()
        self.assertTrue(board.is_occupied(2,0))

if __name__ == '__main__':
    unittest.main()