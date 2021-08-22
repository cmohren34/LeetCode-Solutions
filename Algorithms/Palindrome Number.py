class Solution:
    def isPalindrome(self, x: int) -> bool:
        # save integer as a string, to make reversing easier
        str_x = str(x)
        palin = str_x[::-1]
        
        # if the original string is the same as the reversed string, then palindrome
        if str_x == palin:
            return True
        else:
            return False