def twoSum(nums, target):
    # for i in range(0, len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    dict = {}
    for i in range(0, len(nums)):
        check = target - nums[i]
        if check in dict:
            return [dict[check], i]
        else:
            dict[nums[i]] = i


print(twoSum([3, 2, 4], 6))
