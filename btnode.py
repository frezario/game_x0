"""
Binary tree.
"""


class Node:
    """
    Binary tree Node.
    """

    def __init__(self, data=None, parent=None, right=None, left=None):
        self.parent = parent
        self.right = right
        self.left = left
        self.data = data

    def is_leaf(self):
        """
        Returns True if Node is a leaf and False otherwise.
        """
        return not (self.right or self.left)
