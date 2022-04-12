# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        ll1, ll2, = [], []
        while p1 != None:
            ll1.append(p1.val)
            p1 = p1.next
            
        while p2 != None:
            ll2.append(p2.val)
            p2 = p2.next
        
        a, b, carry = 0, 0, 0
        dummy = ListNode(-1, None)
        prev = dummy
        for i in range(max(len(ll1), len(ll2))):
            a = 0 if i >= len(ll1) else ll1[i]
            b = 0 if i >= len(ll2) else ll2[i]
            
            node_sum = a + b + carry
            if node_sum >= 10:
                carry = 1
                node_sum %= 10
            else:
                carry = 0
                
            new_node = ListNode(node_sum, None)
            prev.next = new_node
            prev = prev.next

            
        # remaining carry-over
        if carry > 0:
            prev.next = ListNode(carry, None)
                
        return dummy.next
