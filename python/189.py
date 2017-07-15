class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:]+nums[:n-k]
        
        
if __name__ == '__main__':
    nums = [1,2]
    k = 1
    print(Solution().rotate(nums,k))