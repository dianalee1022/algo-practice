# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = 0
        current_node = ListNode()
        head = current_node
        carry = 0
        while l1 or l2 or carry:
            number = carry
            if l1:
                number += l1.val
                l1 = l1.next
            
            if l2:
                number += l2.val
                l2 = l2.next

            node_val = number % 10
            carry = number // 10

            current_node.next = ListNode(val=node_val)
            current_node = current_node.next
        
        return head.next

        