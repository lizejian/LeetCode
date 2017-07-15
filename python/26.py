class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
        return cnt+1          
        
        
if __name__ == '__main__':
    nums = [1,2,3,4,6,7,8]
    print(Solution().removeDuplicates(nums))