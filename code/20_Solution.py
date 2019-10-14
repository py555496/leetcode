class Solution(object):
    def isValid(self, s):
        stack = []
        d = {")" : "(", "]" : "[", "}" : "{"}
        for i in s:
            if i == '(' or i =='{' or i == '[':
                stack = [i] + stack
            else:
                if len(stack) == 0:
                    return False
                else:
                    g = stack.pop(0)
                    if g == d.get(i, ""):
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                
        """
        :type s: str
        :rtype: bool
        """