class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        beg, end = -1, -2
        min_num = nums[n-1]
        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[n-1-i])
            if (nums[i] < max_num):
                end = i
            if (nums[n-1-i] > min_num):
                beg = n-1-i
        return end - beg + 1
        
         
if __name__ == '__main__':
    nums = [1,2,4,3,5,7,6,8,9,10,18,17,16,15,14,13,12,11]
    print(Solution().findUnsortedSubarray(nums))