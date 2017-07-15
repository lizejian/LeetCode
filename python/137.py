class Solution():
    def singleNumber(self, nums):
        a = 0
        b = 0
        for c in nums:
            aa = a&(~b)&(~c) | (~a)&b&c
            b = (~a)&b&(~c) | ~a&~b&c
            a = aa
        return b


nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2,-4]
s = Solution()
print s.singleNumber(nums)