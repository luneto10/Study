class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        def dfs(node, left = float("-inf"), right = float("inf")):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root)

s = Solution()
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(s.isValidBST(root))