class Solution(object):
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (x, y)
                for x in range(12) for y in range(60) if bin(x).count('1') + bin(y).count('1') == num]


num = 8
s = Solution()
print s.readBinaryWatch(num)
