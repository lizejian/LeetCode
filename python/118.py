class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        t = [[1]]
        for n in range(numRows - 1):
            t += [list(map(lambda x, y: x + y, t[-1] + [0], [0] + t[-1]))]
        return t[:numRows]
        
        
if __name__ == '__main__':
    print(Solution().generate(5))