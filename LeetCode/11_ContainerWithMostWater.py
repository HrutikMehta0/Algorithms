def maxNaiveArea(heights):
    maxArea = -999999999
    for i in range(0, len(heights)):
        for j in range(i, len(heights)):
            if heights[i] > heights[j]:
                currArea = (j - i) * heights[j]
            else:
                currArea = (j - i) * heights[i]
        if currArea > maxArea:
            maxArea = currArea

    return maxArea


def maxArea(heights):
    pointer_one = 0
    pointer_two = len(heights) - 1
    maximumArea = -99999999
    while pointer_two != 0 or pointer_one != len(heights)-1:
        if heights[pointer_one] > heights[pointer_two]:
            currArea = (pointer_two - pointer_one) * heights[pointer_two]
        else:
            currArea = (pointer_two - pointer_one) * heights[pointer_one]
        if maximumArea < currArea:
            maximumArea = currArea
        pointer_one += 1
        pointer_two -= 1

    return maximumArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
