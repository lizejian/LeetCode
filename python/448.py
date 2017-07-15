class Solution():
    def findDisapearedNumber(self, nums):
        for n in nums:
            idx = abs(n)-1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


nums = [4,3,2,7,8,2,3,1]
s = Solution()
print s.findDisapearedNumber(nums)