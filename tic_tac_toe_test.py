import unittest
from tic_tac_toe_grid import TicTacToeGame


class TicTacToeGameTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_make_move(self):
        # Test making a move
        self.game.make_move(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')

    def test_next_turn(self):
        # Test next turn
        self.game.next_turn()
        self.assertFalse(self.game.is_x_turn)

    def test_win_check(self):
        # Test win check
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        self.game.make_move(0, 1)
        self.game.make_move(2, 2)
        self.game.make_move(0, 2)
        result, _ = self.game.win_check()
        self.assertEqual(result, 'X')

    def test_new_game(self):
        # Test new game
        self.game.make_move(0, 0)
        self.game.new_game(2)
        self.assertEqual(self.game.board, [['', '', ''], ['', '', ''], ['', '', '']])
        self.assertTrue(self.game.is_x_turn)
        self.assertEqual(self.game.count, 0)


if __name__ == '__main__':
    unittest.main()
