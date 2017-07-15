class Solution(object):
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)

  
a = 0
b = -1
s = Solution()
print s.getSum(a, b)
