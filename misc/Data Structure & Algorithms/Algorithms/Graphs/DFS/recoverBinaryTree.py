# Definition for a binary tree node.
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
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        watch_node = []
        def dfs (node, prev, watch_node):
            if not node:
                return
            dfs(node.left, node, watch_node)
            watch_node.append(node)
            dfs(node.right, node, watch_node)
        dfs(root, None, watch_node)
        if len(watch_node) <=1:
            return
        
        swap = []
        for i in range(1,len(watch_node)):
            if len(swap) == 2:
                break
            if watch_node[i - 1].val > watch_node[i].val:
                swap.append(watch_node[i-1])
                swap.append(watch_node[i])
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val
            

s = Solution()
# root = TreeNode(
#     3,
#     left=TreeNode(1),
#     right=TreeNode(4, left=TreeNode(2))
# )
root = TreeNode(
    2,
    left= TreeNode(3),
    right=TreeNode(1)
)
s.recoverTree(root)

                
