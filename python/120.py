class Solution(object):
    def minimumTotal(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        res = A[0]
        for row in A[1:]:
            n = len(row)
            res = [row[0] + res[0]] + [row[i] + min(res[i], res[i-1]) for i in range(1, n-1)] + [row[-1] + res[-1]]
        return min(res)
         
               
if __name__ == '__main__':
    t = [range(1)]
    print(Solution().minimumTotal(t))
    
    