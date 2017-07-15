class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx in range(len(nums)):
            if nums[idx] in d and idx - d[nums[idx]] <= k:
                return True
            d[nums[idx]] = idx                                
        return False

        
if __name__ == '__main__':
    nums = [99, 99]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))