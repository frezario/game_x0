"""
Tree class implementation.
"""
from btnode import Node
from board import Board, next_map

COMP_TOKEN = '0'
USER_TOKEN = 'x'


class Tree:
    """
    Class Tree.
    """

    def __init__(self, board):
        if not isinstance(board, Board):
            board = Board(board)
        self.root = Node(board)

    def build_tree(self, board=None, turn='0', node=None):
        if board is None:
            board = self.root.data
        if node is None:
            node = self.root
        new_turn = USER_TOKEN if turn == COMP_TOKEN else COMP_TOKEN
        moves = Board.get_next_states(board)
        if not moves or board.get_status() != "continue":
            node.right = None
            node.left = None
            return
        if len(moves) == 1:
            node.left = Node(next_map(board, moves[0], turn), node)
        else:
            node.left, node.right = Node(next_map(board, moves[0], turn), node), \
                                    Node(next_map(board, moves[1], turn), node)
        if node.left:
            self.build_tree(node.left.data, new_turn, node.left)
        if node.right:
            self.build_tree(node.right.data, new_turn, node.right)

    def leaves(self, node=None):
        if node is None:
            node = self.root
        leaves = []

        def traversal(node: Node):
            if node.is_leaf():
                leaves.append(node.data)
            else:
                if node.left:
                    traversal(node.left)
                if node.right:
                    traversal(node.right)

        traversal(node)
        # print("LEAVESSSS...")
        return leaves

    def choose_move(self):
        self.build_tree()
        # leaves = self.leaves()
        left_leaves = self.leaves(self.root.left)
        right_leaves = self.leaves(self.root.right)
        count_left = 0
        count_right = 0
        for board in left_leaves:
            if board.get_status() == COMP_TOKEN:
                count_left += 1
            elif board.get_status() == USER_TOKEN:
                count_left -= 1
        for board in right_leaves:
            if board.get_status() == COMP_TOKEN:
                count_right += 1
            elif board.get_status() == USER_TOKEN:
                count_right -= 1
        # Now we have to choose the right move
        new_brd = self.root.left.data if count_left >= count_right else self.root.right.data

        # Searching for a new move
        return new_brd.last_move
        # for row in range(len(new_brd.board)):
        #     for col in range(len(new_brd.board[0])):
        #         if new_brd.board[row][col] != self.root.data.board[row][col]:
        #             return row, col
        # return None

# board = [
#     ['0', '0', 'x'],
#     ['0', 'x', 'x'],
#     [' ', ' ', ' '],
# ]
# tree = Tree(board)
# tree.build_tree()
# # leaves = tree.leaves()
# # print(leaves, len(leaves))
# print(tree.root.data)
# print(tree.choose_move())
# print("LEFT")
# print(tree.root.left.data)
# print("RIGHT")
# print(tree.root.right.data)
# [' ', ' ', ' ']
# [' ', 'x', 'x']
# ['0', '0', ' ']
