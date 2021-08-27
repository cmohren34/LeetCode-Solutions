def sortedSquares(nums: List[int]) -> List[int]:

    nums_squared = []

    # first iterate through the array and square each element
    for x in nums:
        squared = x ** 2
        nums_squared.append(squared) # at the squared element to the end of the new list

    # sort back into ascending order
    nums_squared.sort()

    # return the new list
    return nums_squared