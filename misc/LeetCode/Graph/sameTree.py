from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right) 
    
    def levelOrder(self, root: TreeNode):
        result = [[root.val]]
        visited = set({root})
        queue = deque([root])
        while queue:
            current = queue.popleft()
            layer = []
            if current.left:
                if current.left not in visited:
                    visited.add(current.left)
                    queue.append(current.left)
                    layer.append(current.left.val)
            if current.right:
                if current.right not in visited:
                    visited.add(current.right)
                    queue.append(current.right)
                    layer.append(current.right.val)
            result.append(layer) if layer else None
            
s = Solution()

graph1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
graph2 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
teste = s.isSameTree(graph1, graph2)

graph3 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
teste = s.levelOrder(graph3)