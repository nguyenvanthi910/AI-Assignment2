# ======================== Class Player =======================================
class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    # Student MUST implement this function
    # The return value should be a move that is denoted by a list of tuples:
    # [(row1, col1), (row2, col2), (row3, col3)] with:
    # (row1, col1): current position of selected amazon
    # (row2, col2): new position of selected amazon
    # (row3, col3): position of the square is shot
    def nextMove(self, state):
        result = [(0, 3), (5, 3), (8, 6)]  # example move in wikipedia
        return result


# ======================== Game Object =======================================
WHITE = 'w'
BLACK = 'b'
ARROW = 'X'
EMPTY = '.'
BOARDSIZE = 10

def state_copy(board):
    new_board = [[]]*10
    for i in range(10):
        new_board[i] = [] + board[i]
    return new_board

class Queen:
    TOP = 'TOP'
    TOPLEFT = 'TOPLEFT'
    TOPRIGHT = 'TOPRIGHT'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    BOTTOMLEFT = 'BOTTOMLEFT'
    BOTTOMRIGHT = 'BOTTOMRIGHT'
    BOTTOM = 'BOTTOM'
    def __init__(self, name, row, col, state):
        self.name = name
        self.row = row
        self.col = col
        self.state = state

        # ======== Move of Queen ======

    def movetop(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row - step][self.col] = self.name
        oldrow = self.row
        self.row -= step
        return [(oldrow, self.col), (self.row, self.col)]

    def movedown(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row + step][self.col] = self.name
        oldrow = self.row
        self.row += step
        return [(oldrow, self.col), (self.row, self.col)]

    def moveleft(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row][self.col - step] = self.name
        oldcol = self.col
        self.col -= step
        return [(self.row, oldcol), (self.row, self.col)]

    def moveright(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row][self.col + step] = self.name
        oldcol = self.col
        self.col += step
        return [(self.row, oldcol), (self.row, self.col)]

    def movetopleft(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row + step][self.col - step] = self.name
        oldrow = self.row
        oldcol = self.col
        self.row += step
        self.col -= step
        return [(oldrow, oldcol), (self.row, self.col)]

    def movedownleft(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row - step][self.col - step] = self.name
        oldrow = self.row
        oldcol = self.col
        self.row -= step
        self.col -= step
        return [(oldrow, oldcol), (self.row, self.col)]

    def movetopright(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row + step][self.col + step] = self.name
        oldrow = self.row
        oldcol = self.col
        self.row += step
        self.col += step
        return [(oldrow, oldcol), (self.row, self.col)]

    def movedownright(self, step=1):
        self.state[self.row][self.col] = EMPTY
        self.state[self.row - step][self.col + step] = self.name
        oldrow = self.row
        oldcol = self.col
        self.row -= step
        self.col += step
        return [(oldrow, oldcol), (self.row, self.col)]

    def move(self, direction, step = 1):
        if direction is self.BOTTOM :
            return self.movedownleft(step)
        if direction is self.BOTTOMLEFT:
            return self.movedownleft(step)
        if direction is self.BOTTOMRIGHT:
            return self.movedownright(step)
        if direction is self.LEFT:
            return self.moveleft(step)
        if direction is self.RIGHT:
            return self.moveright(step)
        if direction is self.TOPLEFT:
            return self.movetopleft(step)
        if direction is self.TOP:
            return self.movetop(step)
        if direction is self.TOPRIGHT:
            return self.movetopright(step)

    def canmove(self):
        '''Kiểm tra quân hậu hiện tại có thể di chuyển được không'''
        r = self.row
        c = self.col
        return (r + 1 < 10 and self.state[r + 1][c] == EMPTY) or \
               (r - 1 > -1 and self.state[r - 1][c] == EMPTY) or \
               (c + 1 < 10 and self.state[r][c + 1] == EMPTY) or \
               (c - 1 > -1 and self.state[r][c - 1] == EMPTY) or \
               (r + 1 < 10 and c + 1 < 10 and self.state[r + 1][c + 1] == EMPTY) or \
               (r - 1 > -1 and c + 1 < 10 and self.state[r - 1][c + 1] == EMPTY) or \
               (r - 1 > -1 and c - 1 > -1 and self.state[r - 1][c - 1] == EMPTY) or \
               (r + 1 < 10 and c - 1 > -1 and self.state[r + 1][c - 1] == EMPTY)

    def available(self):
        """
        - - - - -
        + - X - +
        - + + + -
        + + 0 X -
        - + + + -
        [2 1 2 0 1 1 1 2]
        :return:  Danh sách các điểm mà queen có thể đi được theo thứ tự sau
        [topleft, top, topright, right, bottomright, bottom, bottomleft, left]
        """
        result = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, BOARDSIZE):  # TOPLEFT cột giảm hàng tăng
            if self.col < i or self.row + i >= BOARDSIZE: break
            if self.state[self.row + i][self.col - i] == EMPTY:
                result[0] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # TOP hang tang
            if self.row +i >= BOARDSIZE: break
            if self.state[self.row + i][self.col] == EMPTY:
                result[1] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # TOPRIGHT hang va cot tang
            if self.row +i >= BOARDSIZE or self.col + i >= BOARDSIZE: break
            if self.state[self.row + i][self.col + i] == EMPTY:
                result[2] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # RIGHT cot tang
            if self.col + i >= BOARDSIZE: break
            if self.state[self.row][self.col + i] == EMPTY:
                result[3] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # BOTTOMRIGHT cot tang hang giam
            if self.col + i >= BOARDSIZE or self.row < i: break
            if self.state[self.row - i][self.col + i] == EMPTY:
                result[4] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # BOTTOM hang giam
            if self.row < i : break
            if self.state[self.row - i][self.col] == EMPTY:
                result[5] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # BOTTOMLEFT hang giam cot giam
            if self.row < i or self.col < i: break
            if self.state[self.row - i][self.col - i] == EMPTY:
                result[6] += 1
            else:
                break
        for i in range(1, BOARDSIZE):  # LEFT cot giam
            if self.col < i: break
            if self.state[self.row][self.col - i] == EMPTY:
                result[7] += 1
            else:
                break
        return result

    def __shot__(self, row, col):
        self.state[row][col] = ARROW
        return (row, col)

    def shottopleft(self, step = 1):
        return self.__shot__(self.row +  step, self.col - step)

    def shottop(self, step = 1):
        return self.__shot__(self.row + step, self.col)

    def shottopright(self, step = 1):
        return self.__shot__(self.row + step, self.col + step)

    def shotright(self, step = 1):
        return self.__shot__(self.row, self.col + step)

    def shotbottomright(self, step = 1):
        return self.__shot__(self.row - step, self.col + step)

    def shotbottom(self, step = 1):
        return self.__shot__(self.row - step, self.col)

    def shotbottomleft(self, step = 1):
        return self.__shot__(self.row - step, self.col - step)

    def shotleft(self, step = 1):
        return self.__shot__(self.row, self.col - step)

    def shot(self, direction, step = 1):
        if direction is self.TOPLEFT:
            return self.shottopleft(step)
        if direction is self.TOP:
            return self.shottop(step)
        if direction is self.TOPRIGHT:
            return self.shottopright(step)
        if direction is self.RIGHT:
            return self.shotright(step)
        if direction is self.BOTTOMRIGHT:
            return self.shotbottomright(step)
        if direction is self.BOTTOM:
            return self.shotbottom(step)
        if direction is self.BOTTOMLEFT:
            return self.shotbottomleft(step)
        if direction is self.LEFT:
            return self.shotleft(step)

def get_gamenode(name, state):
    """Khởi tạo game node từ state và name"""
    lsqueens = []
    for row in range(10):
        for col in range(10):
            if state[row][col] == name:
                lsqueens.append([row, col])
    return GameNode(name, lsqueens, state)

class GameNode:
    def __init__(self, name, lsqueen, state):
        self.name = name
        self.queens = []
        self.state = state
        for i,j in lsqueen:
            self.queens.append(Queen(self.name, i, j, state_copy(state)))
        self.lsmoves = [queen.available() for queen in self.queens]
        self.moves = sum([sum(i) for i in self.lsmoves])
        self.parent = None
        self.children = []
        self.result = None
    def get_instance(name, state):
        """Khởi tạo game node từ state và name"""
        lsqueens = []
        for row in range(10):
            for col in range(10):
                if state[row][col] == name:
                    lsqueens.append([row, col])
        return GameNode(name, lsqueens, state)

class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, myname, othername, state):
        self.root = GameNode.get_instance(myname, state)
        for queen in self.root.queens:
            

    def parse_subtree(self, data_list, parent):
        if type(data_list) is list:
            leaf_node = GameNode(data_list[0])
            leaf_node.parent = parent
            parent.addChild(leaf_node)
            if len(data_list) == 2:
                leaf_node.value = data_list[1]
            return
        tree_node = GameNode(data_list(0))
        tree_node.parent = parent
        parent.addChild(tree_node)
        for elem in data_list:
            self.parse_subtree(elem, tree_node)
        return

    def nextMove(self, state):
        result = [(0, 3), (5, 3), (8, 6)]  # example move in wikipedia
        return result

    def Minimax(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print("AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
        print("AlphaBeta:  Best State is: " + best_state.Name)
        return best_state
