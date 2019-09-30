class Solution(object):
    def is_palind(self,s):
        if s == s[::-1]:
            return True
        else:
            return False
    def longestPalindrome(self, s):
        max_leng = 0
        max_s = ""
        for i in range(len(s)):
            #如果存在双回文，先计算双回文
            if i + 1 < len(s) and s[i + 1] == s[i]:
                step = 1
                while i - step > -1 and i + step + 1 < len(s):
                    if s[i - step] == s[i + 1 + step]:
                        step += 1
                    else:
                        break;
                leng = (step - 1) * 2 + 2
                if max_leng < leng:
                    max_leng = leng
                    max_s = s[i - (step - 1): i + step + 1]
            #单回文
            step = 1
            while i - step > -1 and i + step < len(s):
                if s[i - step] == s[i + step]:
                    step += 1
                else:
                    break
            leng = 2 * step - 1
            if max_leng < leng:
                max_leng = leng
                max_s = s[i - (step - 1): i + step]
        return max_s
        """
        :type s: str
        :rtype: str
        """
        