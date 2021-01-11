from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        d = deque()
        d.append((root, 1))

        levels = []
        cur_level = []
        prev_level = 1

        while len(d) > 0:
            node, level = d.popleft()

            if level != prev_level:
                levels.append(cur_level)
                cur_level = []
                prev_level = level

            cur_level.append(node.val)

            if node.left is not None:
                d.append((node.left, level + 1))

            if node.right is not None:
                d.append((node.right, level + 1))

        if len(cur_level) > 0:
            levels.append(cur_level)

        levels.reverse()

        return levels
