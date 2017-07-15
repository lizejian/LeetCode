class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        res = [1]
        for _ in range(rowIndex):
            res = list(map(lambda x, y: x + y, res + [0], [0] + res))
        return res

if __name__ == '__main__':
    print(Solution().getRow(0))