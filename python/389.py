class Solution(object):
    def findTheDifference(self, s, t):
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if dic.get(c, 0) == 0:
                return c
            else:
                dic[c] -= 1


s = Solution()
print s.findTheDifference('a', 'aa')
