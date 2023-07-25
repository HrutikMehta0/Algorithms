def threeSum(nums):
    nums = sorted(nums)
    finalArr = []
    dict = {}
    for i in range(0, len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            print("Hi")


threeSum([-1, 0, 1, 2, -1, -4])
