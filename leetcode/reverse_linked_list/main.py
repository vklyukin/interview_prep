# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        curr = None
        while head:
            tmp = ListNode(head.val)
            head = head.next
            tmp.next = curr
            curr = tmp
        return curr
