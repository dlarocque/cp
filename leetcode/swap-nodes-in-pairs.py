class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        nxt = curr.next
        while curr.next:
            tmp = nxt.next
            nxt.next = curr
            curr.next = tmp
            prev.next = nxt

            prev = curr
            curr = curr.next
            if not curr: break
            nxt = curr.next

        return dummy.next
