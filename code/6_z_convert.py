class Solution(object):
    def convert(self, s, numRows):
        if s == "":
            return ""
        if numRows == 1:
            return s
        d = {}
        c = 0
        rever = True
        for g in s:
            if not c in d:
                d[c] = []
            d[c].append(g)
            if rever:
                c += 1
            else:
                c -= 1
            if c == numRows - 1:
                rever = False
            elif c == 0:
                rever = True
        out = ""
        print sorted(d.keys())
        for i in sorted(d.keys()):
            out += "".join(d[i])
        return out
                
            
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        