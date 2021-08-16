# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next: # removing the only node in the list
            return None

        dummy = ListNode(0, head)
        size = 0
        linked_list = [] # storing the linked list nodes in a list

        while head:
            linked_list.append(head)
            size += 1
            head = head.next

        # remove the (size - n)th node from the list
        if n == size: # removing the first node
            dummy.next = linked_list[0].next
            linked_list[0].next = None
        elif n == 1: # removing the last node
            linked_list[size-2].next = None
        else:
            linked_list[size-n-1].next = linked_list[size-n+1]

        return dummy.next

