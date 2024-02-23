def missingNumber(nums):
    nums_set = set(nums)
    for i in range(0, len(nums)+1):
        if i not in nums_set:
            return i


print(missingNumber([0,1]))
