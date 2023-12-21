# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # We use two pointers
        # 1) prev -> which will hold what the node will point to
        # 2) curr -> the node that is being changed to point to prev
        prev = None 
        curr = head

        # We loop till the linked list has been fully traversed 
        while curr:
            # Store the next node for reassignment
            # Then Let the node point to the previous node 
            # Reassign prev to now be the appointed node
            # Reassign curr to be the next node we saved in tmp
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # We return prev as when are done the node we end on is now the start
        return prev