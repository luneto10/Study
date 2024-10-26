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


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_binary_tree(arr, index: int = 0):
    """
    Recursively builds a complete binary tree from the array.

    :param arr: List of integer values.
    :param index: Current index in the array.
    :return: Root node of the binary tree.
    """
    if index >= len(arr):
        return None

    # Create the current node
    root = Node(arr[index])
    print(f"Creating {root} at index {index}")

    # Recursively build the left and right subtrees
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    print(f"Left child of {root.val} will be at index {left_index}")
    root.left = build_binary_tree(arr, left_index)

    print(f"Right child of {root.val} will be at index {right_index}")
    root.right = build_binary_tree(arr, right_index)

    return root


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    def minDepthBFS(self, root: TreeNode) -> int:
        from collections import deque

        visited = set()
        queue = deque([root])
        visited.add(root.val)
        precedors = {root.val: None}
        leafs = []
        paths = float("inf")
        while queue:
            current = queue.popleft()
            if current.left and current.left not in visited:
                visited.add(current.left.val)
                queue.append(current.left)
                precedors[current.left.val] = current.val
            if current.right and current.right not in visited:
                visited.add(current.right.val)
                queue.append(current.right)
                precedors[current.right.val] = current.val
            if not current.left and not current.right:
                leafs.append(current.val)

        for leaf in leafs:
            i = 0
            while leaf != None:
                leaf = precedors[leaf]
                i += 1
            paths = min(paths, i)
        return paths

    def minDepthDFS(self, root: TreeNode) -> int:
        min_depth = float("inf")

        def dfs(root, current_depth=1):
            nonlocal min_depth
            if not root:
                return 1

            if root.left is None and root.right is None:
                min_depth = min(min_depth, current_depth)

            dfs(root.left, current_depth + 1)
            dfs(root.right, current_depth + 1)

        dfs(root)

        return min_depth

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum

    def pathSum(self, root: TreeNode, targetSum: int) -> bool:
        result = []

        def dfs(root, targetSum, path):
            if not root:
                return

            path.append(root.val)
            if not root.left and not root.right:
                if targetSum == root.val:
                    result.append(path[:])
            dfs(root.left, targetSum - root.val, path)
            dfs(root.right, targetSum - root.val, path)
            path.pop()

        dfs(root, targetSum, [])
        return result

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []

        def dfs(root):
            if not root:
                return
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        root.left = None
        root.right = None
        current = root
        for node in result:
            current.right = TreeNode(node)
            current = current.right
        root = root.right

    def connect(self, root):
        def helper(root, parent):
            if root is None:
                return
            if parent is not None:
                parent.left.next = parent.right
            if parent is not None and parent.next is not None:
                parent.right.next = parent.next.left
            if root.left is None and root.right is None:
                return
            helper(root.left, root)
            helper(root.right, root)

        helper(root, None)
        return root


s = Solution()
root = TreeNode(
    3, left=(TreeNode(9)), right=(TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
)
# root = TreeNode(2)
# root.right = TreeNode(3)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(5)
# root.right.right.right.right = TreeNode(6)
# root = TreeNode(-2)
# root.right = TreeNode(-3)
# root = TreeNode(
#     1,
#     left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
#     right=TreeNode(5, right=TreeNode(6)),
# )

root = Node(
    1,
    left=Node(2),
    right=Node(3),
)
binary_tree = build_binary_tree([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(s.connect(binary_tree))
