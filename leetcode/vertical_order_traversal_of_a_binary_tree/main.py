# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.tree_vertices = []

    def verticalTraversalHelper(self, node: TreeNode, x: int, y: int):
        if node is None:
            return

        self.tree_vertices.append(((x, y), node.val))

        self.verticalTraversalHelper(node.left, x - 1, y - 1)
        self.verticalTraversalHelper(node.right, x + 1, y - 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.verticalTraversalHelper(root, 0, 0)

        self.tree_vertices.sort(key=lambda x: (x[0][0], -x[0][1], x[1]))

        traversal_order = []
        traversal_level = []
        prev_x = 0

        for (x, y), value in self.tree_vertices:
            if traversal_level and prev_x < x:
                traversal_order.append(traversal_level)
                traversal_level = []

            traversal_level.append(value)
            prev_x = x

        if traversal_level:
            traversal_order.append(traversal_level)

        return traversal_order
