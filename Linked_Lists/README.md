Note: This section will have code based on leetcode's systems and as such does not work locally. To simulate similar ideas we would define our own linked list structure :)

# 19. Remove Nth Node From End of List

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

- Have a fast pointer accelerated by "n" places as that would mean when passing through the slow pointer would be the node before the one you want to remove
- Remove it by passing over it -> This does not delete it and would still have to deallocate it
- Essentially you are doing len - (len - n) = n which is the position you want to be in when passing

# 21. Merge Two Sorted Lists

Link: https://leetcode.com/problems/merge-two-sorted-lists/

- Use of dummy variable to keep track of the start of the list
- Rest of the logic is comparing the two nodes from each list and seeing which one is smaller so we can add that

# 141. Linked List Cycle

Link: https://leetcode.com/problems/linked-list-cycle/

- Idea is using Flyod's Tortoise and Hare
- This is when if we have a pointer that is moving through the list twice as fast, it will reach null eventually before the slow one
- And when it does not that means that its cycled possibly somewhere

# 143. Reorder List

Link: https://leetcode.com/problems/reorder-list/

- Find the middle with two pointers -> a fast and a slow pointer
- Split the list into two lists with the second list you are reversing due to the alternating condition
- Merge the two lists together

# 206. Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/

- Have two pointers to allow for swapping
- First pointer holds the current node
- Second pointer holds the previous node
- Make current point to previous and repeat
