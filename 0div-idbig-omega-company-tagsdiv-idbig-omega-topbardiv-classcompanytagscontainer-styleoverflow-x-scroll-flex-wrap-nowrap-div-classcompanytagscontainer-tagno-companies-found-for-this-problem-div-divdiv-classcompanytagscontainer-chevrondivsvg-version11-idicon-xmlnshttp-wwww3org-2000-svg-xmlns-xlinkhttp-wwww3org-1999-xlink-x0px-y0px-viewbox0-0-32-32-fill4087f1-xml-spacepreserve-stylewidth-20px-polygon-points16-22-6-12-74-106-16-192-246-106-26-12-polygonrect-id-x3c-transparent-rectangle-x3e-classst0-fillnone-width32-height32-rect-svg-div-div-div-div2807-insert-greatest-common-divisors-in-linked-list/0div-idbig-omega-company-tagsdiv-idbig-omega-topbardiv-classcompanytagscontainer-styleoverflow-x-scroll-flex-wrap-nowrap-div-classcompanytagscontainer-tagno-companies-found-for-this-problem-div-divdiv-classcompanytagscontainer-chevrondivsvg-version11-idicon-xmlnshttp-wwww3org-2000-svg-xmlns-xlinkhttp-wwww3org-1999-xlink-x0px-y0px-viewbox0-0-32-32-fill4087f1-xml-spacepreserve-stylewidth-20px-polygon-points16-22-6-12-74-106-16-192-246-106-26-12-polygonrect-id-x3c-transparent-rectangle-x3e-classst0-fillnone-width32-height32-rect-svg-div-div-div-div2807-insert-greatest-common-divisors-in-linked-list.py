# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a,b):
            while b:
                a, b= b, a%b
            return a
        if not head and head.next:
            return head
        curr= head
        while curr and curr.next:
            val= gcd(curr.val,curr.next.val)
            new_node= ListNode(val)
            new_node.next= curr.next
            curr.next= new_node
            curr = new_node.next
        return head
        