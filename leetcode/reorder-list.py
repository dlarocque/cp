# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        mid = n//2
        for i in range(n):
            if i == mid:
                nodes[i].next = None
                continue

            if i < n//2 or mid == -1:
                nodes[i].next = nodes[n-1-i]
            else:
                nodes[i].next = nodes[n-i]


        return head


