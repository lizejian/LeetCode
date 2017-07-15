class Solution():
    def numberOfArithmeticSlices(self, A):
        n = 0
        diff = A[1]-A[0]
        nums = [0, 0]
        for i in range(2, len(A)):
            if A[i]-A[i-1] == diff:
                n += 1
                nums.append(nums[i-1]+n)
            else:
                diff = A[i]-A[i-1]
                n = 0
                nums.append(nums[i-1])
        return nums[len(A)-1]


A = [1, 2, 3, 4, 5]
s = Solution()
print s.numberOfArithmeticSlices(A)