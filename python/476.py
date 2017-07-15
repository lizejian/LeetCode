class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        while i <= num:
            i <<= 1
        return (i - 1) ^ num

if __name__ == '__main__':
    print(Solution().findComplement(5))