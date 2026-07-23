# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        first = second = 0
        digit = 1
        while l1: 
            if l1.val:
                first = first + (l1.val * digit)
            l1 = l1.next
            digit *= 10

        print(first)
        
        digit = 1
        while l2:
            if l2.val:
                second = second + (l2.val * digit)
            l2 = l2.next
            digit *= 10
        print (second)
        result = first + second
        current = None
        for i in str(result):
            next_node = current
            current = ListNode(val=int(i), next=next_node)
        
        return current
        