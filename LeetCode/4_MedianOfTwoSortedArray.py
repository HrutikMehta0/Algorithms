import math


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    arr = []
    i = j = k =0
    while i<len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j+=1

    while i < len(nums1):
        arr.append(nums1[i])
        i+=1
    while j < len(nums2):
        arr.append(nums2[j])
        j+=1
    if len(arr) % 2 == 0:
        median = (arr[(len(arr)//2)] + arr[(len(arr)//2)-1])/2
    else:
        median = arr[(len(arr)//2)]
    return median




print(findMedianSortedArrays([1, 2], [3,4]))
