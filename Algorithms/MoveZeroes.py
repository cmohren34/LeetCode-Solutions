from typing import List

def moveZeroes(nums: List[int]) -> None:
    # do not return anything, modify nums in place

    for x in nums:
        if x == 0:
            nums.remove(0)
            nums.append(0)


nums = [0,10,3,12]

moveZeroes(nums)
print(nums)
