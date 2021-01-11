# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ansList = []
        while l1 != None or l2 != None or ans != None:
            digit = 0
            if l1 != None and l2 != None:
                digit = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                digit = l1.val
                l1 = l1.next
            elif l2 != None:
                digit = l2.val
                l2 = l2.next
            digit += ans.val
            ans.val = digit
            ans.val %= 10
            ansList.append(ans.val)
            if digit > 9:
                ans.next = ListNode(1)
            elif l1 != None or l2 != None:
                ans.next = ListNode(0)
            ans = ans.next
        return ansList
