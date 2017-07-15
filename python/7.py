from functools import reduce

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        flag = 1 + -2*(x < 0)
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        result = flag * result
        if result > 2147483647 or result < -2147483648:
            return 0
        return flag*result
        
            
if __name__ == '__main__':
    print(Solution().reverse(1534236469))