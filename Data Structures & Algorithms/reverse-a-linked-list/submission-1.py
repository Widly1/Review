# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # declare our pointers for 
        # prev node 
        prev = None
        
        # our current node
        current = head

        # as long as current pointer isnt null do the following:
        while current:
            # declare our next node ahead of time for traversal and reversal
            nexxt = current.next 
            
            # flip our arrow for the reversal process (making the next look at prev instead)
            current.next = prev
            
            # move prev to the current node we just finished reversing the arrow for 
            prev = current

            # then move our current pointer to the next node
            current = nexxt
        
        # lastly return prev since its the new head of the list
        return prev 





