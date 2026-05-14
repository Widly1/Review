# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # we will need 2 variables
        prev, current = None, head 
        
        while current:
            # 1. LOOK AHEAD: Save the next node so we don't lose the rest of the list 
            # when we disconnect the current node.
            temp = current.next

            # 2. FLIP: Change the current node's pointer to point BACKWARDS 
            # to the previous node instead of forwards.
            current.next = prev

            # 3. SET PREVIOUS: Move the 'prev' marker up to the current node. 
            # This node is now the "backwards" target for the next step.
            prev = current

            # 4. STEP UP: Move the 'curr' marker to the node we saved in 'temp'. 
            # We are now ready to repeat the process on the next node.
            current = temp
        
        return prev