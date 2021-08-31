from typing import List

# will be solved using two pointer algorithm aka sliding glass door 
# similiar to binary search 
# this also works because it can take advantage of the fact that they are
# already sorted, that should be a keyword to use this algorithm 

def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0   # start the left pointer at the beginning of list
    j = len(numbers) - 1    # right pointer at the end of the list

    # while the left pointer has yet to reach the right pointer
    while i < j:
        if numbers[i] + numbers[j] == target:
            break # goal
        # if it is less than the target, then slide the leftmost pointer up one
        elif numbers[i] + numbers[j] < target:
            i += 1
        # this can just be an else statement but did an elif for explicity 
        elif numbers[i] + numbers[j] > target:
            j -= 1

    # return the index + 1 due to submission criteria 
    return [i+1, j+1]