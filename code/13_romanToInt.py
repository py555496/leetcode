class Solution(object):
    def romanToInt(self, s):
        char_d = {'M': 1000, 'D':500, 'CM' : 800, 'CD': 300, 'C':100, 'L':50, 'XC' : 80, 'XL' : 30, 'X':10, 'V':5, 'IX' : 8, 'IV': 3, 'I':1}
        return sum([char_d.get(s[max(i - 1,0): i + 1], char_d[s[i]]) for i in range(len(s))])
       
        """
        :type s: str
        :rtype: int
        """