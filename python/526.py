class Solution():
    def countArrangement(self, N):
        memo = {(1,(x,)):1 for x in range(1,N+1)}
        def helper(i, X):
            key = (i,X)
            try:
                return memo[key]
            except KeyError:
                num = 0
                for j in range(len(X)):
                    if not X[j] % i or not i % X[j]:
                        num += helper(i-1, X[:j]+X[j+1:])
            return num
        return helper(N, tuple(range(1,N+1)))


s = Solution()
print s.countArrangement(4)