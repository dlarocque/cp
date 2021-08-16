# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)

        h = [node.val for node in lists if node]
        heapq.heapify(h)

        dic = {} # key = node value, val = list of nodes that follow nodes with node.val
        for node in lists:
            if node and node.next:
                if node.val in dic: dic[node.val].append(node.next)
                else: dic[node.val] = [node.next]

        curr = dummy
        while h:
            val = heapq.heappop(h)

            next_node = None
            if val in dic and len(dic[val]) > 0:
                next_node = dic[val][0]
                dic[val] = dic[val][1:]

                heapq.heappush(h, next_node.val)
                heapq.heapify(h)

                if next_node.next:
                    if next_node.val in dic: dic[next_node.val].append(next_node.next)
                    else: dic[next_node.val] = [next_node.next]


            node = ListNode(val, None)
            curr.next = node
            curr = curr.next

        return dummy.next
