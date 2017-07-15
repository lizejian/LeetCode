import collections
class Solution(object):
    def subsetsWithDup(self, nums):
        c = collections.Counter(nums)
        res = [[]]
        for x in c:
            temp = []
            for i in range(1, c[x]+1):
                for j in range(len(res)):
                    temp.append(res[j] + [x]*i)
            res += temp
        return res
        
if __name__ == '__main__':
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))