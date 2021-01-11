# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def traverse(
            root: TreeNode, first=None, second=None, prev=TreeNode(float("-inf"))
        ):
            if root is None:
                return first, second, prev
            first, second, prev = traverse(root.left, first, second, prev)

            if root.val <= prev.val and first is None:
                first = prev
            if root.val <= prev.val and first is not None:
                second = root

            prev = root
            return traverse(root.right, first, second, prev)

        first, second, _ = traverse(root)
        first.val, second.val = second.val, first.val