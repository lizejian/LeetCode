class Solution():
    def minMoves2(self, nums):
        n = sorted(nums)[len(nums)/2]
        return sum([abs(n-item) for item in nums])


nums = [1, 3, 2]
s = Solution()
print s.minMoves2(nums)
