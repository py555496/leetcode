# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def linktonum(self,l1):
        a = l1.val
        multi_num = 10
        while l1.next:
            a = l1.next.val * multi_num + a
            multi_num *= 10
            l1 = l1.next
        return a
    def numtolink(self, num):
        a = num % 10
        head = ListNode(a)
        num = num / 10
        b = head
        # 8 0 7
        while num:
            a = num % 10
            p = ListNode(a)
            b.next = p
            b = p
            num = num / 10
        return head
        
    def addTwoNumbers(self, l1, l2):
        n1 = self.linktonum(l1)
        n2 = self.linktonum(l2)
        s = n1 + n2
        n = self.numtolink(s)
        return n
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        