# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        p = ListNode(head.val)
        p.next = head.next
        for i in range(n):
            p = p.next
        d = ListNode(head.val)
        d.next = head.next
        if p == None:
            head = head.next
        elif p.next == None:
            head.next = head.next.next
        else:
            while not p.next == None:
                p = p.next
                d = d.next
            d.next = d.next.next
        return head
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """