# ============= Solution 1 ============== #
# For this we can set two variables 
# And to visualise it if we had an array of numbers [1, 2 , 3 , 4, 5]
# The idea is we always analyse three variables each time, first, second and n
# In the array above, first = 1, second = 2 and n = 3
# Thus each time we see if either first + n is the max or just second as these will fit into the 
# constraints of not allowing for adjacent houses to be robbed
#
# We want to advance the window forward each time 
# So we then set first to be the second
# Second to then be at `n`
# And `n` getting the new number
# As second will be the last postion we can just return that at the end
# 
# With this method we are constantly retaining the previous values and reusing it allowing ust
# To add up all the numbers to get the max amount that can be robbed
def rob(nums) -> int:
    first = 0
    second = 0

    for value in nums:
        temp = max(first + value, second)
        first = second
        second = temp
    
    return second

# ========== Solution 2 ============ #
# We will slowly build a more optimal solution with the next few solutions
# We define a function and recurse on it with our options either being i - 2 + nums[i] or i - 1 as being the viable path
# Continue going deeper through the array till we reach the end and unwrap resolving each step 
# This then allows us to find the value on the final return
# This is a bit too slow so we will have to fix it
def rob(nums) -> int:
    def step(nums, index):
        if index < 0:
            return 0
        return max(step(nums, index - 2) + nums[index], step(nums, index - 1))
        

    return step(nums, len(nums) - 1)

# ========== Solution 3 ============ #
# On this version we utilise caching or memoisation to reuse old values
# We first set up the array that we will be reusing
# And now modify our step function to instead return early if we already have calculated that value
# But also everytime we perform a calculation check at a step we would store it in the array for later use
# It unravels the same as above but its more optimised with the cache so we only have to look at thigns once rather than repeat calculations
def rob(nums) -> int:
    memo = [-1] * len(nums)
    
    def step(nums, index):
        if index < 0:
            return 0
        
        if memo[index] >= 0:
            return memo[index]

        result = max(step(nums, index - 2) + nums[index], step(nums, index - 1))
        memo[index] = result
        return result
    
    return step(nums, len(nums) - 1)

