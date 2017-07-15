class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        if len(s) < 3:
            return max(s)
        s = s.remove(max(s))
        s = s.remove(max(s))
        return max(s)
        
        
if __name__ == '__main__':
    nums = [ 2, 2, 3, 1]
    print(Solution().thirdMax(nums))