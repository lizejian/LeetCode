class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        i, j, di, dj = 0, 0, 0, 1
        while cnt <= n**2:
            grid[i][j] = cnt
            cnt += 1
            if i + di == n or j + dj == n or grid[i + di][j + dj]:         
                di, dj = dj, -di
            i += di
            j += dj
        return grid

        
if __name__ == '__main__':
    print(Solution().generateMatrix(3))