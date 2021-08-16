"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.generateNode(node, {})

    def generateNode(self, node, dic):
        # generate the node and recursively generate all of the adjacent nodes
        if not node:
            return None

        if node.val in dic:
            return dic[node.val]

        new_node = Node(node.val)
        dic[node.val] = new_node
        new_node.neighbors = [self.generateNode(adj, dic) for adj in node.neighbors]

        return new_node


