class Solution(object):
    def totalHammingDistance(self, nums):
        total = 0
        while True:
            memo = [0, 0]
            zero = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero += 1
                memo[nums[i] % 2] += 1
                nums[i] >>= 1
            total += memo[0]*memo[1]
            if zero == len(nums):
                return total



nums = range(0, 10000)
s = Solution()
print s.totalHammingDistance(nums)
