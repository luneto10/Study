class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def binary_tree(arr: list) -> TreeNode:
    head = TreeNode(val=arr[0])
    current = head

    for i in range(1, len(arr)):
        while True:
            if arr[i] < current.val:
                if current.left == None:
                    new_node = TreeNode(val=arr[i])
                    current.left = new_node
                    break
                else:
                    current = current.left
            elif arr[i] > current.val:
                if current.right == None:
                    new_node = TreeNode(val=arr[i])
                    current.right = new_node
                    break
                else:
                    current = current.right
            else:
                break
        current = head
    return head

arr = [7, 4, 10, 11, 9, 1,]
node = binary_tree(arr)
def pretty_print(node: TreeNode, prefix: str = "", is_left: bool = True):
    """
    Recursively prints the binary tree in a visually appealing way.
    
    Args:
        node (Optional[TreeNode]): The current node to print.
        prefix (str): The prefix string for current node's position.
        is_left (bool): Flag indicating if the node is a left child.
    """
    if node is not None:
        # Print the right subtree first
        pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        
        # Print the current node
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.val))
        
        # Print the left subtree
        pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)

pretty_print(node)

