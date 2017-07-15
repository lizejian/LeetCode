class Solution():
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(31)[::-1]:
            answer <<= 1
            prefixes = {n >> i for n in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer


nums = range(10000)
s = Solution()
print s.findMaximumXOR(nums)
