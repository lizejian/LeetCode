class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        m = 1
        for n in nums:
            output.append(m)
            m = m * n
        m = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= m
            m = m * nums[i]
        return output            
        
        
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))