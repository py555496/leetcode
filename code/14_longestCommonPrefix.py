class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        m = min([len(x) for x in strs])
        g_arr = []
        index = ""
        flag = True
        for i in range(m):
            for g in strs:
                g_arr.append(g[i])
            #print g_arr
            if len(set(g_arr)) == 1:
                g_arr = []
            else:
                index = strs[0][:i]
                flag = False
                break
        if flag:
            return strs[0][:m]
        else:
            return index
            
            
        """
        :type strs: List[str]
        :rtype: str
        """