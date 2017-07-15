class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = -2*31
        stack = []
        for s1 in nums[::-1]:
            if s1 < s3:
                return True
            while stack and stack[-1] < s1:
                s3 = stack[-1]
                stack.pop()
            stack.append(s1)
        return True
        
        
if __name__ == '__main__':
    nums = [-1, 3, 2, 0]
    print(Solution().find132pattern(nums))