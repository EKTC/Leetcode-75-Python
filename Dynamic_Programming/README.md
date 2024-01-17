# 55. Jump Game

Link: https://leetcode.com/problems/jump-game/description/

- The first solution is to do something really nice which is to always track how far you can reach
- Thus if we ever find out our reach cannot move past the current index we can return False
- Else we continue through and start changing our reach to be the current value or a new value based on the new index we just reached
- The second method is similar to a greedy approach in which instead we will work in reverse
- For this we think of it as the target or goal being the last index which we want to reach
- But if we think about it we have to reach it from some node so we check to find the first index that can reach it
- Now we see that the plan is not to reach the end but now reach this new index that reaches the end so we can shift our goal / target up
- We can keep doing this till we reach the 1st index which would be 0 and return True
- Note: Both methods above run in O(n) time unlike the DP approach
- The last method is using DP which will take up O(n) space but also be O(n^2) in terms of time complexity
- The gist of the method is to save whether you can continue further with the current node you are at and store that so when it comes back up again we dont have to recalculate this is super slow

# 62. Unique Paths

Link: https://leetcode.com/problems/unique-paths/description/

- We notice that the robot can only move down or right
- Meaning to reach a square there are only two other squares that can reach it
- Thus if we know the ways to get to those two squares we can find the way to reach the target square we want
- And then we continue going through the algorithm till we reach the end
- Base case is that the first two squares next to the start must be 1 to start of the algorithm

# 70. Climbing Stairs

Link: https://leetcode.com/problems/climbing-stairs/

- We will use memoisation to store the values at each step that leads up to the number of steps
- We go backwards till we exhaust all the paths
- We know that theres only two options we go up 1 step or go up 2 steps so we account for those at that current level we are at
- Base cases is that there is 1 path to get to value 1 and 2 paths to get to value 2

# 139. Word Break

Link: https://leetcode.com/problems/word-break/

- The idea is that you want to have another array that can store the bounds of possible words and chain them together
- You have a base case of setting one to "True" to allow the rest of the string to be checked

# 198. House Robber

Link: https://leetcode.com/problems/house-robber/description/

- We define the recurrence as that given an index of `i` we can either rob `i - 1` or `i + (i - 2)`
- We can then store or have the values from previous iterations to be used for our calculations as we basically always have a scope of 3 values
- The recurrence would have no base case

# 213. House Robber II

Link: https://leetcode.com/problems/house-robber-ii/description/

- This is similar to house robber which was done before but we realise that due to the circular adjacency there is a couple of edge cases
- Instead we should bound the ranges and perform the algorithm to find the max for each bound
- Thus we can find the max amount to rob

# 322. Coin Change

Link: https://leetcode.com/problems/coin-change/description/

- Use of previous amount value calculations such that we find all previous values so we can use later on
- Base case of 0
