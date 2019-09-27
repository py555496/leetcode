"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        out_list = []
        node_stack = []
        node_stack = [root] + node_stack
        while len(node_stack) > 0:
            out_node = node_stack.pop(0)
            out_list += [out_node.val]
            for node in out_node.children[::-1]:
                node_stack = [node] + node_stack
        return out_list
        """
        :type root: Node
        :rtype: List[int]
        """
        