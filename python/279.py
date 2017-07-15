class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        for i in range(n):
            if i ** 0.5 == int(i ** 0.5):
                memo[i] = 1
            elif i % :
                
            
            

if __name__ == '__main__':
    print(Solution().numSquares(12))