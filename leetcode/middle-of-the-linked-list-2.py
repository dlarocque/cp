# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Iterate over the linked list until we reach the end, 
        storing all nodes in a list
        2. return the node at (n//2)
        
        
        n = 6
        [x,x,x,x,x,x]
        
        """
        nodes = [None] * 100
        
        temp, i = head, 0
        while temp:
            nodes[i] = temp
            i += 1
            temp = temp.next
            
        return nodes[i//2]
            
