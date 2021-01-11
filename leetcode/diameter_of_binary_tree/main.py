# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self._diameter_helper(root)
        return self.max_diameter

    def _diameter_helper(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_diameter = self._diameter_helper(root.left)
        right_diameter = self._diameter_helper(root.right)

        self.max_diameter = max(self.max_diameter, left_diameter + right_diameter)

        return 1 + max(left_diameter, right_diameter)
