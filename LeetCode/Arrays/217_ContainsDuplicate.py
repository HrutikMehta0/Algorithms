def containsDuplicate(nums):
    dict = {}
    for i in range(0, len(nums)):
        if nums[i] in dict:
            return True
        else:
            dict[nums[i]] = nums[i]
    return False


print(containsDuplicate([3, 3]))
