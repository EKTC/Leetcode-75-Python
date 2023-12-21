# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy basically sits at the start as a pointer
        # So we can easily return the new built list
        # Temp variable on the other hand is the one moving and slowly adding
        # The new nodes
        temp = dummy = ListNode()
        
        # We loop till one of the lists end
        while list1 and list2:
            # Check if list1 or list2 has the bigger value
            # And add the smaller node
            # Move on to the next nodes of the respective list and the temp list
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        # When we reach the end one of the lists just append the remaining elements
        # From the non empty list
        # And finally return the list but next so we remove our placeholder from the start
        temp.next = list1 or list2
        return dummy.next