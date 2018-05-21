import unittest
from amazons import get_gamenode
from amazons import GameNode
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

class GameNodeTest(unittest.TestCase):
    def test_getinstance(self):
        state = Initial_Board
        node = GameNode.get_instance("w", state)
        self.assertEqual(node.lsmoves, [[0, 0, 0, 2, 5, 8, 2, 3],
                                        [0, 0, 0, 3, 2, 8, 5, 2],
                                        [0, 3, 2, 8, 5, 2, 0, 0],
                                        [2, 3, 0, 0, 0, 2, 5, 8]])
        self.assertEqual(node.moves, 80)