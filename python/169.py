def majorityElement(nums):
    count = 0
    res = 0
    for num in nums:
        if not count:
            res = num
            count = 1
        elif res ^ num:
            count -= 1
        else:
            count += 1
    return res


print majorityElement([1,1,2,3,1,3,1])
