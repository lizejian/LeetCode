class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits))[::-1]:
            digits[i] = (digits[i] + 1) % 10
            if digits[i]:
                return digits
        return [1] + digits        
            
        
if __name__ == '__main__':
    print(Solution().plusOne([0]))
    print(Solution().plusOne([9,9,9]))