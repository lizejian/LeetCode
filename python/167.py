class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d:
                return [d[numbers[i]] + 1, i + 1]
            d[target - numbers[i]] = i

            
if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 17
    print(Solution().twoSum(numbers, target))