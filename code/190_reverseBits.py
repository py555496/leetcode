class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(str(bin(n)[2:]).zfill(32)[::-1],2)
        