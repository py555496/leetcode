class Solution(object):
    def hammingWeight(self, n):
        #function 1   24ms 11mb
        """
        a = []
        while n > 0:
            a.append(n % 2)
            n = n / 2
        return sum(a)
        """ 
        # function 2  12ms 11.7mb 
        s = 0
        #print str(n)
        for i in str(bin(n)):
            if i == '1':
                s += 1
        return s
        """
        :type n: int
        :rtype: int
        """
        