# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Have two pointers
        # If we move the fast pointer by n 
        # Thus when we move both pointers later the
        # Fast pointer will be at the end whilst the slow pointer will be right before the node we want to remove
        slow = fast = head 

        # This code is pushing the pointer forward
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # Edge case where n is the length of the list and that means we remove the head and thus
        # Just return head.next effeectively removing the node but not deleting it
        if not fast:
            return head.next

        # Shifting the pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Removing the node but not deleting
        slow.next = slow.next.next
        return head