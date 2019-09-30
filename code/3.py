class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        i = 0
        st = {} #st记录重复字符在窗口中最后面的位置eg 'acfstf' 中遇到f时需要找到f
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
            
        """
        :type s: str
        :rtype: int
        """
        