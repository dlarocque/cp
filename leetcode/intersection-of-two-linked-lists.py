# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = {}
        
        # iterate through headB
        while headB:
            if headB: nodes[headB] = True
            headB = headB.next
            
        while headA:
            if headA in nodes: return headA
            else: headA = headA.next
                
        return None
        
