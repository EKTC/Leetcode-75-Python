# ========== Solution ============= #
# Its performing mergesort for the logic
# Hence we would perform merging of two lists constantly till we get one list
# The logic here is that if we merge two lists each time it would reduce the amount of lists `n` to then be `log n`
# We would still need to go through each list so its `n` work
def mergeKLists(lists):
    
    # This function helps us perform the merging of two lists
    def mergeTwoLists(list1, list2):
        
        temp = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        temp.next = list1 or list2
        return dummy.next

    # ======== Main Function Code ========== #
    
    # Edge Case
    if len(lists) == 0:
        return None

    # Loop till we get one list which means all other lists have been merged
    while len(lists) > 1:
        
        # Keep track of all merged list for each iteration here
        temp_merged_lists = []
        # Loop for two elements each time
        for index in range(0, len(lists), 2):
            l1 = lists[index]
            l2 = None
            # Check if we actually have another list to use in merging otherwise leave it empty
            if index + 1 < len(lists):
                l2 = lists[index + 1]
            
            temp_merged_lists.append(mergeTwoLists(l1, l2))
            
        lists = temp_merged_lists # Reassign it to continue looping
    return lists[0]