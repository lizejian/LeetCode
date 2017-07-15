class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        total = duration*len(timeSeries)
        for i in range(1, len(timeSeries)):
            total -= max(0, duration - (timeSeries[i]-timeSeries[i-1]))
        return total


t = [1, 4]
d = 2
s = Solution()
print s.findPoisonedDuration(t, d)
