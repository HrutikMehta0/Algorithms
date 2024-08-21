def canJump(nums):
    max_reach = 0
    i = 0
    while i < len(nums) and i <= max_reach:
        max_reach = max(max_reach, i + nums[i])
        print(max_reach)
        if max_reach >= len(nums) - 1:
            return True
        i += 1
    return False


# Test Cases
print(canJump([2, 3, 1, 1, 4]))  # Output: True
print(canJump([3, 2, 1, 0, 4]))  # Output: False
