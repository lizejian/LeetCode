class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return i+1

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    print(Solution().searchInsert(nums, 7))