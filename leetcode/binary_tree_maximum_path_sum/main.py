# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = float("-inf")

    def maxPathSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_path_left = self.maxPathSubtree(root.left)
        max_path_right = self.maxPathSubtree(root.right)

        self.max_path = max(
            self.max_path,
            max_path_left + max_path_right + root.val,
            max_path_left + root.val,
            max_path_right + root.val,
        )

        return root.val + max(0, max_path_left, max_path_right)

    def maxPathSum(self, root: TreeNode) -> int:
        max_path_root = self.maxPathSubtree(root)
        return max(max_path_root, self.max_path)
