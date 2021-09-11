# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# NOTE: that the Nth node means the (k-n) where k is the amount of nodes in the linked list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # just as clarification the nth node from the end is
        # the (k-n)th node
        # wil be done using the 2 pointer alrogrithm
        
        # while the node ahead is not empty 
        while(head.next != None):
            temp_list = ListNode(-1)
            left = temp_list
            left_n = temp_list
            
            left.next = head
            left_n.next = head  # will be considered the node that is moving "fast"
            
            # we do plus one because range goes up until but not including
            for i in range(n+1):
                left_n = left_n.next    # incrementing by one
            
            # until left_n reaches the end of the linked list
            while left_n:
                left = left.next    # increment the "slow" pointer by 1
                left_n = left_n.next    #increment again by 1
                
            left.next = left.next.next  # increments again to catch up
            
            return temp_list.next   # now you return the linked list that has been created without the (k-n)th node
            
            
        
        