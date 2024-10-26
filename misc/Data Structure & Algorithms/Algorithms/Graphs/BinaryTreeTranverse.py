class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def visited(root:TreeNode, result=[]):
    result.append(root.val)
def preorderTraversal(root: TreeNode, result = []):
    if root:
        visited(root, result)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)
    return result

def inorderTraversal(root: TreeNode, result = []):
    if root:
        inorderTraversal(root.left, result)
        visited(root, result)
        inorderTraversal(root.right, result)
    return result
        
def postorderTraversal(root: TreeNode, result=[]):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        visited(root, result)
    return result
binaryTree = TreeNode("A", left=TreeNode("B", left=TreeNode("D"), right=TreeNode("E")), right=TreeNode("C", right=TreeNode("F")))

print(f"Preorder Traversal: \n{preorderTraversal(binaryTree)}\n")

print(f"Inorder Traversal: \n{inorderTraversal(binaryTree)}\n")

print(f"Postorder Traversal: \n{postorderTraversal(binaryTree)}\n")