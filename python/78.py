class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res


nums = [1,2,4]
s = Solution()
print s.subsets(nums)