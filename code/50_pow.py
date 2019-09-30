class Solution(object):
    def myPow(self, x, n):
        if x < 1e-10 and x > 0:
            return 0
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return float(1) / self.myPow(x, -n)
        else:
            if n % 2 == 0:
                return self.myPow(x * x, n / 2) 
            else:
                return x * self.myPow(x * x, (n - 1) / 2)
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        