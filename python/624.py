class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result, max_num, min_num = 0, arrays[0][-1], arrays[0][0]
        for array in arrays[1:]:
            result = max(result, abs(array[-1]-min_num))
            result = max(result, abs(max_num-array[0]))
            max_num = max(max_num, array[-1])
            min_num = min(min_num, array[0])
        return result
    
        
if __name__ == '__main__':
    arrays = [[1,2,3], [4,5], [1,2,3]]
    s = Solution()
    print(s.maxDistance(arrays))
