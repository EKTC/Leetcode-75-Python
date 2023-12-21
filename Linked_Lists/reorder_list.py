# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # First is to get to the middle of the list
        # We use fast.next and fast.next.next as we want the majority
        # Of the elements to always be in the first list -> the list we are not reversing
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Variables to reverse the list
        reverse = slow.next
        prev = None
        # This one is done to uncouple the first list with the second list and hence are separate 
        # Ie: [1, 2, 3, 4] splits into [1, 2, 3] and [3, 4] so we do this line to only get [1, 2]
        slow.next = None 
        
        # Reverse a linked list :(
        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp
        
        # Setup new heads for merging the lists
        h1 = head
        h2 = prev

        # ===================== METHOD 1 =================== #
        
        # This one looks a bit more abstract but lets dive into it
        # We store list1's other nodes 
        # Reassign list1's current node to be the alternate from list2
        # We then let list1 to become list2
        # And then we set list2 to become list1
        # Hence we are switching which node we are adding as now 
        # We are adding a node from list2 but that has become list1 !!!
        # Crazy strat
        while h2:
            tmp = h1.next
            h1.next = h2
            h1 = h2
            h2 = tmp
        
        # ===================== METHOD 2 =================== #
        
        # We store the next nodes of both lists
        # We then assign the alternating element for list1
        # And then follow that up with list1 elements for list2
        # We then reassign the elements to have its next elements allowing us to iterate through the list
        # To break it down here you are adding an element from list2 then reassigning the rest of list1 to it
        # Whilst keeping the original list1 and list2 but just incremented to get the next variable
        while h2:
            h1_temp = h1.next
            h2_temp = h2.next

            h1.next = h2
            h2.next = h1_temp

            h1 = h1_temp
            h2  = h2_temp