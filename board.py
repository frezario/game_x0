"""
Board class implementation.
"""
import copy


# from btree import USER_TOKEN, COMP_TOKEN, Tree

class Board:
    """
    Board class.
    """

    def __init__(self, board=None, last_move=None):
        if board is not None:
            assert len(board) == 3 and len(board[0]) == len(board[1]) == len(board[2]) == 3, \
                "Bad board"
            self.board = board
        else:
            self.board = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' '],
            ]
        if last_move is not None:
            assert len(last_move) == 2 and len(last_move[1]) == 2, "Bad move"
        self.last_move = last_move

    def get_status(self):
        """
        Checks a state of the game.
        Returns a special string for each of possible states.
        """
        # Checking rows
        for symbol in 'x', '0':
            for line in self.board:
                line = list(line)
                if line.count(symbol) == 3:
                    return symbol
            # Checking cols
            if (symbol, symbol, symbol) in zip(self.board[0], self.board[1], self.board[2]):
                return symbol
            # Checking diagonals
            for _ in range(0, 3):
                if self.board[_][_] != symbol:
                    break
                if _ == 2:
                    return symbol

            for _ in range(0, 3):
                if self.board[_][2 - _] != symbol:
                    break
                if _ == 2:
                    return symbol
        # Checking for draw
        for line in self.board:
            if ' ' in line:
                return "continue"
        return "draw"

    def make_move(self, position: tuple, turn: str):
        """
        Makes a move if it is possible, raises IndexError otherwise.
        """
        assert len(position) == 2, "Bad position"
        if self.board[position[0]][position[1]] != ' ':
            raise IndexError("Bad move")
        self.board[position[0]][position[1]] = turn
        self.last_move = position

    @staticmethod
    def get_next_states(board=None):
        """
        Returns two possible states of the next map.
        """
        moves = []
        for row in range(3):
            for col in range(3):
                if len(moves) == 2:
                    return moves
                if board.board[row][col] == ' ':
                    moves.append((row, col))
        return moves

    def make_computer_move(self):
        tree = Tree(self)
        tree.build_tree()
        return tree.choose_move()

    def __repr__(self):
        return repr(self.board[0]) + '\n' + repr(self.board[1]) + '\n' + repr(self.board[2])


def next_map(board: Board, move: tuple, turn):
    """
    Builds next map.
    """
    new_brd = copy.deepcopy(board)
    new_brd.make_move(move, turn)
    return new_brd


if __name__ == "__main__":
    brd = [['0', '0', '0'],
           ['x', ' ', 'x'],
           [' ', ' ', 'x'],
           ]
    b = Board(brd)
    print(b.get_status())
    print(b)
