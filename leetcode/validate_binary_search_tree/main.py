# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root: TreeNode, lower=float("-inf"), upper=float("inf")):
            if root is None:
                return True

            if root.val >= upper or root.val <= lower:
                return False

            children = True
            children &= traverse(root.left, lower, root.val)

            if not children:
                return False

            children &= traverse(root.right, root.val, upper)
            return children

        return traverse(root)