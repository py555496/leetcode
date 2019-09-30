class Solution(object):
    def reverse(self, x):
        out = 0
        if x == 0:
            return 0
        elif x > 0:
            out = int(str(x)[::-1])
            return 0 if out > 2147483647 else out
        else:
            out = -int(str(x)[1:][::-1])
            return 0 if out < -2147483648 else out
        """
        :type x: int
        :rtype: int
        """
        