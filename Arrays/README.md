# 1. Two Sum

Link: https://leetcode.com/problems/two-sum/

- Idea is to check each number for its corresponding sum in a dictionary
- If it is not there add it to the dictionary and continue

# 11. Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water/

- Binary search once more
- Has some conditions to check such as calculating the max area and which height is the minimum of the two

# 15. 3Sum

Link: https://leetcode.com/problems/3sum/description/

- Idea is similar to two sum question
- This is where we sort the array and perform binary search to get the numbers that lead to the sum
- However now that there is a third number we want to first pick a number as our start and then binary search for a value that can make it zero involving that zero number
- Thus it becomes a binary search with a set a value that changes as we go iterate through the array

# 33. Search in Rotated Sorted Array

Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

- Binary search but modified again
- Key idea is to cover the edge cases again based on whether the pivot is part of the right or left array
- And then doing a binary search again on that to see if its left or right

# 53. Maximum Subarray

Link: https://leetcode.com/problems/maximum-subarray/description/

- The idea is to ignore negative prefixes as they dont contribute to producing a max sum
- Always check when adding a number for the max sum

# 121. Best Time to Buy and Sell Stock

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

- We setup two pointers one for buying and one for selling
- Based on the values we would either update the buying pointer to be the lowest amount of the two pointers
- Or the right pointer to move
- Calculate the profits as we iterate through

# 152. Maximum Product Subarray

Link: https://leetcode.com/problems/maximum-product-subarray/

- We have a variable to store the final value
- But a variable to store max and variable to store min of the current sums
- We then check based on the 3 variables

# 153. Find Minimum in Rotated Sorted Array

Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

- A binary search that is a bit modified
- Has more checks based on edge cases that can occur

# 169. Majority Element

Link: https://leetcode.com/problems/majority-element/description/

- Use a set to get all the unique elements
- Loop through to find the majority element which was a given condition

# 217. Contains Duplicate

Link: https://leetcode.com/problems/contains-duplicate/

- Iterates through the array and storing all the seen numbers in a set
- If there is already a number in the set we can return

# 238. Product of Array Except Self

Link: https://leetcode.com/problems/product-of-array-except-self/description/

- Idea is to calculate the prefix which is all the operands before the specified number
- And then calculate the postfix which is all the operands after the specified number
- Combine them together
- V2 is a more optimised version that mutates them in the array itself rather than seperating it

# 278. First Bad Version

Link: https://leetcode.com/problems/first-bad-version/description/

- So we use binary search but with some extra context we can make it faster and skip through some of the values
- The key is to track with the left and right pointers and shifting them up when needed to reduce the search space
- For this case if its a bad version we know we want an earlier one if possible so we can shift the right pointer back
- And the opposite for the left one which is more tracking the good versions

# 704. Binary Search

Link: https://leetcode.com/problems/binary-search/description/

- Implementation of binary search a core to a lot of problems in a sense
- The idea is that we have a left and right pointer and we shift them based on our `target`
- We have a `mid` variable that is based off the values at the left and right pointer
- If `mid` is bigger than `target` that means our value is to large and we shift our right pointer down to find a smaller value and vice versa for the smaller case
- Loop till we traverse the entire array or if we find the value

# 733. Flood Fill

Link: https://leetcode.com/problems/flood-fill/description/

- The implementation is around a DFS, in which we recursively check each cell
- We then modify the cell if it meets the condition otherwise we dont
- Implementation of a visited array is possible to prevent infinite looping
