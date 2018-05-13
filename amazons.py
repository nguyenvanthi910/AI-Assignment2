
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

class GameNode:
    def __init__(self,name,value=0,parent=None):
        self.Name = name
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self,childNode):
        self.children.append(childNode)

class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data_list):
        self.root = GameNode(data_list.pop(0))
        for elem in data_list:
            self.parse_subtree(elem,self.root)

    def parse_subtree(self,data_list,parent):
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
            self.parse_subtree(elem,tree_node)
        return

    def nextMove(self, state):
        result = [(0,3),(5,3),(8,6)] # example move in wikipedia
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
        print "AlphaBeta:  Utility Value of Root Node: = " + str(best_val)
        print "AlphaBeta:  Best State is: " + best_state.Name
        return best_state