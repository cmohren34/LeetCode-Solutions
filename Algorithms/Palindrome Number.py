class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        palin = string[::-1]
        
        # if the parsed strings are equal to each other it is a palindrome
        if string == palin:
            return True
        else:
            return False