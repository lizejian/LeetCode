class Solution(object):
    def canPlaceFlowers(self, A, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0) and (i == len(A)-1 or A[i+1] == 0)):
                n -= 1
                A[i] = 1                
        return n <= 0
                
        
if __name__ == '__main__':
    flowerbed = [1,0,0,0]
    print(Solution().canPlaceFlowers(flowerbed, 1))