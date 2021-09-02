# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize two pointers at the beginning of the list
        # one that will increment by 1 and the other by 2
        
        left = head
        left_fast = head
        
        # then we iterate until fast's head has reached the end
        
        # so while these are true, b/c when they are null it will be the end
        while left_fast and left_fast.next:
            left = left.next
            left_fast = left_fast.next.next    # increments by 2
            
        # next we know that when the fast pointer is done,
        # the slow pointer will have reached the middle of the linked list
        
        return left