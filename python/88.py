class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)
       

if __name__ == '__main__':
    nums1 = [1, 2, 4]
    m = 3
    nums2 = [2, 5, 9]
    n = 4
    print(Solution().merge(nums1, m, nums2, n))