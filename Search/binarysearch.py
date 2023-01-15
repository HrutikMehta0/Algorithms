def search(nums, target) -> int:
    lo = 0
    hi = len(nums) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    if nums[lo] == target:
        return lo
    elif nums[hi] == target:
        return hi
    else:
        return -1


print(search([0, 1, 2, 4, 5, 6, 7], 4))
