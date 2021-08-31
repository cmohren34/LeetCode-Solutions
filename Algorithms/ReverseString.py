from typing import List

def reverseString(s: List[str]) -> None:
    # we have to reverse the list in-place
    # which just means not to make any copies

    # here are some one liners that you can do 
    s.reverse()

    # or
    # this will change all the elements in the list to the
    # reverse of the items already in the list
    s[:] = s[::-1]