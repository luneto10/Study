class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        """
        Returns a string representation of the TreeNode for easier debugging.
        """
        return f"TreeNode({self.data})"