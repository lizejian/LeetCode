class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
            print(nums)
        
if __name__ == '__main__':
    nums = [0, 1, 0,2, 3, 12]
    print(Solution().moveZeroes(nums))