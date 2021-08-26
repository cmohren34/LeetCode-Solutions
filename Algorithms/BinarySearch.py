from typing import List

def search(nums : List[int], target : int) -> int:
    # working off the index
    low = 0
    high = len(nums) - 1
    mid = 0

    # run until the list is empty
    while low <= high:
        mid = (high + low) // 2

        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            return mid
        
    # if the element is not present at all
    return -1

nums = [-1,0,3,5,9,12]
target = 9
result = search(nums, target)

if result != -1:
    print("\n The target was found at position ", result, "\n")
else:
    print("\nThe target was not found\n")