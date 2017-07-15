class Solution(object):
    def majorityElement(self, nums):
        if len(nums) < 2:
            return nums
        res1, res2 = 0, 1
        count1, count2 = 0, 0
        for n in nums:
            if res1 == n:
                count1 += 1
            elif res2 == n:
                count2 += 1
            elif count1 == 0:
                res1 = n
                count1 = 1
            elif count2 == 0:
                res2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (res1, res2) if nums.count(n) > len(nums)/3]


nums = [3,0,3,4]
s = Solution()
print s.majorityElement(nums)
