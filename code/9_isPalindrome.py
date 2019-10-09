class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        i = 0
        flag = True
        while True:
            if not s[i] == s[len(s) - i - 1]:
                flag = False
                break
            i += 1
            if i > len(s) / 2:
                break
        return flag
        """
        :type x: int
        :rtype: bool
        """
        