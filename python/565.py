class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, cnt, n = 0, 0, len(nums)
        flag = [False] * n
        for i in range(n):
            while not flag[i]:
                flag[i] = True
                i, cnt = nums[i], cnt + 1
            res = max(res, cnt)
            cnt = 0
        return res
                
        
        
if __name__ == '__main__':
    A = [5,4,0,3,1,6,2]
    print(Solution().arrayNesting(A))