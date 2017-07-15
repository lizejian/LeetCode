class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        head, tail = 0, m * n - 1
        while head <= tail:
            mid = (head + tail) >> 1
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            elif num > target:
                tail = mid - 1
            else:
                head = mid + 1
        return False
                
if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print(Solution().searchMatrix(matrix, 50))