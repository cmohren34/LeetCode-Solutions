def searchInsert(nums: List[int], target: int) -> int:

    # normal binary search process
    low = 0 
    high = len(nums) - 1
    middle = 0

    while low <= high:
        middle = (high + low) // 2

        if target < nums[middle]:
            high = middle - 1
        elif target > nums[middle]:
            low = middle + 1
        elif target == nums[middle]:
            return middle

    # if it was not found in the list
    else:
        nums.append(target)
        nums.sort()

        return nums.index(target)

    # this was more of a lazy way of doing it but, if i was being more
    # technical I would create a copy of the list and then do this