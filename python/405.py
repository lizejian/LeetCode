class Solution(object):
    def toHex(self, num):
        mask = 0xFFFFFFFF
        def helper(x):
            return ''.join('0123456789abcdef'[(num >> 4*i) & 15] for i in range(8)[::-1]).lstrip('0') or '0'
        return helper(num) if num >= 0 else helper(num & mask)


num = -2
s = Solution()
print s.toHex(num)
