class Solution(object):
    def findRepeatedDnaSequences(self, s):
        memo = {}
        res = []
        for i in range(len(s)-9):
            subSquence = s[i:i+10]
            if memo.get(subSquence, 0) == 1:
                res.append(subSquence)
            else:
                memo[subSquence] = memo.get(subSquence, 0) + 1
        return res


s = "AAAAAAAAAAAA"
solution = Solution()
print solution.findRepeatedDnaSequences(s)
