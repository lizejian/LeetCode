class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        d = collections.Counter(nums)
        if k == 0:    
            result = sum(d[v] > 1 for v in d)
        else:
            result = sum(n - k in d for n in d)
        return result

            
if __name__ == '__main__':
    nums = [1,3,1,5,4]
    k = 0
    print(Solution().findPairs(nums, k))