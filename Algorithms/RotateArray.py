from typing import List
from collections import deque

def rotate(nums: List[int], k: int) -> None:
    # do not return anything, modify nums in place

    # do up until 0 or else there will be an extra move
    while k > 0:

        # insert the popped item from nums before the 0 index
        # all elements after that item are shifted to the right
        nums.insert(0, nums.pop())

        k -= 1
        





nums = [1,2,3,4,5,6,7]

rotate(nums, 3)

# check answer
print(nums)