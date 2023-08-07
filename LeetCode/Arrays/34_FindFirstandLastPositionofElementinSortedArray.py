def searchRange(nums, target):
    start = len(nums) // 2
    while start < 0 or start > len(nums):
        print(nums)


searchRange([5, 7, 7, 8, 8, 10], 10)
