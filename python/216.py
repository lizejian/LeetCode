class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 45 or n < k*(k+1)//2:
            return []               
        def dfs(res, arr, beg, k, n):
            if k == 0:
                if n == 0:
                    res.append(list(arr))
                return                
            for i in range(beg, min(10, n+1)):
                arr.append(i)
                dfs(res, arr, i + 1, k - 1, n - i)
                arr.pop()     
        res = []
        dfs(res, [], 1, k, n)
        return res
                
        
if __name__ == '__main__':
    print(Solution().combinationSum3(3, 9))