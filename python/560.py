class Solution(object):
    def subarraySum(self, A, K):
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su-K]
            count[su] += 1
        return ans
        
        
if __name__ == '__main__':
    nums = [1,2]
    print(Solution().subarraySum(nums, 2))