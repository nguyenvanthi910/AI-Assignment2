import unittest
from amazons import Queen
Initial_Board = [
    ['.', '.', '.', 'w', '.', '.', 'w', '.', '.', '.'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['w', '.', '.', '.', '.', '.', '.', '.', '.', 'w'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['b', '.', '.', '.', '.', '.', '.', '.', '.', 'b'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
    ['.', '.', '.', 'b', '.', '.', 'b', '.', '.', '.'], \
    ]
class QueenTest(unittest.TestCase):
    state = Initial_Board
    b1 = Queen('b', 6, 0, state)

    def test_available(self):
        self.assertEqual(self.b1.available(), [0, 2, 5, 8, 2, 3, 0, 0])

    def test_movetop_default_step(self):
        state = Initial_Board
        b1 = Queen('b', 6, 0, state)
        b1.movetop()
        self.assertEqual(b1.state[6][0], '.')
        self.assertEqual(b1.state[5][0], 'b')

    def test_movetop_step_2(self):
        state = Initial_Board
        b1 = Queen('b', 6, 0, state)
        b1.movetop(2)
        self.assertEqual(b1.state[6][0], '.')
        self.assertEqual(b1.state[4][0], 'b')

    def test_movedown_default_step(self):
        state = Initial_Board
        b1 = Queen('b', 6, 0, state)
        b1.movedown()
        self.assertEqual(b1.state[6][0], '.')
        self.assertEqual(b1.state[7][0], 'b')

    def test_movedown_step_2(self):
        state = Initial_Board
        b1 = Queen('b', 6, 0, state)
        b1.movedown(2)
        self.assertEqual(b1.state[6][0], '.')
        self.assertEqual(b1.state[8][0], 'b')