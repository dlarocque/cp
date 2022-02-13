# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        
        n = len(nodes)
        
        if n % 2 == 0:
            return nodes[n//2:] == nodes[:n//2][::-1]
        else:
            return nodes[n//2:] == nodes[:n//2+1][::-1]
            
