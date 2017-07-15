class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder

                
if __name__ == '__main__':
    nums = [3,4,1,6,2,5,7,8,6]
    print(Solution().findDuplicate(nums))