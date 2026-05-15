# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create our temp pointer to keep track of when we reach the end of our new list
        temp =  ListNode()
        tail = temp

        # iterate though both lists
        while list1 and list2:
            # check the values to see which is smaller and should be next in new lists
            if list1.val < list2.val:
                # make tail.next our smaller node for the next link
                tail.next = list1
                # move our current pointer to the next node in our list for comparison
                list1 = list1.next
            else: # same process as list1 but for list2
                tail.next = list2
                list2 = list2.next
            # move our pointer forward
            tail = tail.next
        
         # edge cases for empty lists
        if list1 is None:
            tail.next = list2
        elif list2 is None:
            tail.next = list1
        
        return temp.next