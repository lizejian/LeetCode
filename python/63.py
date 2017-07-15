class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        if not grid or grid[0][0]:
            return 0
        m, n = len(grid), len(grid[0])
        grid[0][0] = 1
        for i in range(1, m):
            if not grid[i][0]:
                grid[i][0] = grid[i - 1][0]
            else:
                grid[i][0] = 0
        for j in range(1, n):
            if not grid[0][j]:
                grid[0][j] = grid[0][j - 1]
            else:
                grid[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]
      

if __name__ == '__main__':
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(grid))