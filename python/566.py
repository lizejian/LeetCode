class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        allnums = [nums[i][j] for i in range(len(nums))[::-1] for j in range(len(nums[0]))[::-1]]
        newMat = [[allnums.pop() for j in range(c)] for i in range(r)]
        return newMat   
        
        
if __name__ == '__main__':
    nums = [[1, 2], [3, 4], [5, 6], [7, 8]]
    r = 2
    c = 4
    print(Solution().matrixReshape(nums, r, c))