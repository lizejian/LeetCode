class Solution():
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res


nums = [4,3,2,7,8,2,3,1]
s = Solution()
print s.findDuplicates(nums)
