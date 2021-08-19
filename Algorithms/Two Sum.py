# for this problem, give a list of integers from input, you have to return the 2 indices that 
# add up to the sum of the target number (also from input)
# for example: if you are give a list that is [2,7,11,15] and the target = 9
#    then you would return [0,1] because 2+7 = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using the enumerate function here to seperate index and value
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i >= j: continue
                if num1 + num2 == target: 
                    return[i,j]

# here enumerate is used to make a tuple that gives the (index,value)
# mem usage: 14.7 mb
# runtime: O(n^2)
# space: O(1)