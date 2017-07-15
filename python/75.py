class Solution(object):
    def sortColors(self, nums):
        red, white, blue = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                blue += 1
                nums[blue] = 2
                white += 1
                nums[white] = 1
                red += 1
                nums[red] = 0
            elif nums[i] == 1:
                blue += 1
                nums[blue] = 2
                white += 1
                nums[blue] = 1
            else:
                blue += 1
                nums[blue] = 2
        return nums
        
if __name__ == '__main__':
    nums = [2,2,1,1,0,0]
    print(Solution().sortColors(nums))