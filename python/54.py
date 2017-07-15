class Solution(object):
    def spiralOrder(self, A):
        if not A:
            return []
        m, n = len(A), len(A[0])
        res = []
        cnt = 0
        i, j, di, dj = 0, 0, 0, 1
        while cnt < m * n:
            res.append(A[i][j])
            A[i][j] = None
            cnt += 1
            if i + di == m or j + dj == n or A[i + di][j + dj] == None:
                di, dj = dj, -di
            i += di
            j += dj
        return res
            
        
if __name__ == '__main__':
    matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    print(Solution().spiralOrder(matrix))