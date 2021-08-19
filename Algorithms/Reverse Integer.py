# in this situtation you are given a sequence of integers and are asked to reverse them, however
# if it excedes the given bounds you must print out a 0

class Solution:
    def reverse(self, x: int) -> int:
        # successfully returning a reveresed string greater than 0
        str_x = str(x)
        rev_string = str_x[::-1]
        
        # if it was a negatively signed integer and it now ends in an integer after being reversed
        
        if rev_string[-1] == '-':
            rev_x = -1 * int(rev_string[:-1])
        else:
            rev_x = int(rev_string)
        
        # if reversing the integer made it go outside of the given bounds
        
        if rev_x < -(2**31) or rev_x > 2**31 - 1:
            return 0
        elif rev_x > 2**31 - 1:
            return 0
        else:
            return rev_x