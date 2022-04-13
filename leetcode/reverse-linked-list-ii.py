# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        curr, end = head, None
        while curr:
            n += 1
            if not curr.next:
                end = curr
            curr = curr.next
            
        end.next = head
        
        curr = head
        k %= n
        for i in range(n-k-1):
            curr = curr.next
          
        print(curr.val)
        head = curr.next
        curr.next = None
        return head
