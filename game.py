"""
Game implementation.
"""
from board import Board
from btree import COMP_TOKEN, USER_TOKEN, Tree


class Game:
    """Game class"""

    def __init__(self):
        self.board = Board()

    def run(self):
        token = USER_TOKEN
        print(self.board)
        while self.board.get_status() == "continue":
            if token == USER_TOKEN:
                player_move = input("ENTER A MOVE: ")
                player_move = player_move.split(' ')
                player_move = tuple(int(pos) for pos in player_move)
                while True:
                    try:
                        self.board.make_move(player_move, token)
                        break
                    except IndexError:
                        print("Wrong move, try again...")
            else:
                print("COMPUTER'S TURN: ")
                tree = Tree(self.board)
                tree.build_tree()
                comp_move = tree.choose_move()
                self.board.make_move(comp_move, token)
            # Printing map
            print(self.board)
            # Changing token
            token = COMP_TOKEN if token == USER_TOKEN else USER_TOKEN
        winner = self.board.get_status()
        if winner == "draw":
            print("Draw!")
        else:
            print(f"{winner} is the winner!")


if __name__ == '__main__':
    game = Game()
    game.run()
