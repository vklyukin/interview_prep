# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        treeStack = []

        if root != None:
            treeStack.append(root)

        while len(treeStack) > 0:
            node = treeStack.pop()
            answer.append(node.val)

            if type(node.right) is not type(None):
                treeStack.append(node.right)

            if type(node.left) is not type(None):
                treeStack.append(node.left)
        return answer