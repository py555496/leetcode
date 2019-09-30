# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2list(self, root):
        index = 1
        a = [[root,index]]
        out_d = {}
        while a:
            b, index = a.pop(0)
            if not index in out_d:
                out_d[index] = 0
            out_d[index] += b.val
            if b.left:
                a.append([b.left, index + 1])
            if b.right:
                a.append([b.right, index + 1])
        return out_d
    def maxLevelSum(self, root):
        out_d = self.tree2list(root)
        m_n = -1
        index = -1
        for k, v in out_d.items():
            if v > m_n:
                m_n = v
                index = k
        return index
        """
        :type root: TreeNode
        :rtype: int
        """
        