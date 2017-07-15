class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, big * n, small * n), min(n, big * n, small * n)
            res = max(res, big)
        return res
        
        
if __name__ == '__main__':
    nums = [.2,.3,-0.02,.4,.4]
    print(Solution().maxProduct(nums))