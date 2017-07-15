class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[m] = nums[i]
                m += 1
        return m

        
if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums, val))