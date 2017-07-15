class Solution(object):
    def integerReplacement(self, n):
        memo = {1: 0}
        def helper(num):
            try:
                return memo[num]
            except KeyError:
                if num % 2 == 0:
                    total = 1 + helper(num >> 1)
                else:
                    addOne = helper(num+1)
                    minOne = helper(num-1)
                    total = 1 + min(addOne, minOne)
                memo[num] = total
                return total
        return helper(n)


n = 10000000
s = Solution()
print s.integerReplacement(n)
