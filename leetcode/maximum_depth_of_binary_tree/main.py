# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []

        if not root:
            return 0

        maxD = 0
        stack.append((root, 1))

        while stack:
            node = stack.pop()

            if node[1] > maxD:
                maxD = node[1]

            if node[0].right:
                stack.append((node[0].right, node[1] + 1))

            if node[0].left:
                stack.append((node[0].left, node[1] + 1))

        return maxD
