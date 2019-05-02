def max(nums):
    """Returns the `index` of the largest number in a list. If two or more indices share
    the same largest value, we return the first one we find. If nums is not a list, or if nums
    contains no values, return -1."""
    maximum = 0
    i = 0
    while i < len(nums)-1:
        if nums[i] >= maximum:
            maximum = nums[i]
        i += 1
    return maximum

