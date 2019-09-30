# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        out_list = []
        node_stack = []
        #push
        node_stack = [root] + node_stack
        while len(node_stack) > 0:
            out_node = node_stack.pop(0)
            out_list += [out_node.val]
            if out_node.right:
                node_stack = [out_node.right] + node_stack
            if out_node.left:
                node_stack = [out_node.left] + node_stack
        return out_list
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        