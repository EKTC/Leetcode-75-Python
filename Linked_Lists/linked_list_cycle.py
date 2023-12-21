# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Start both pointers at the start
        slow = head
        fast = head

        # Checks if we have a valid fast current node and it has a next node to allow for a 
        # double move to the next next node
        while fast and fast.next:
            # Slow moves once whislt fast moves twice as fast
            slow = slow.next
            fast = fast.next.next
            
            # If the node equals at any point that means that 
            # The fast has cycled and caught the slow pointer in moving and thus cycle
            if slow is fast:
                return True
        
        return False