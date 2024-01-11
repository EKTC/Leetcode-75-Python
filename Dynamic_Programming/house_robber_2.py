# ========== Solution 1 ========== #
# This is similar to Hosue robber one 
# Instead we bound two ranges to perform our search on
#
# Given an example of [1, 2, 3, 4, 5]
# We can notice that if we take 5 we cannot take 1 as they would be adjacent
# But we can take anything at 2 till the 5
# On the reverse if we take 1 we now cannot take 5 but can take anything inbetween till 4
#
# So that we have this we just take the max between out of the two paths
# In addition without caching it is too slow so we will use memoisation
# But have to recognise that they will actually be different values based on the lists 
# So have two separate possible ranges of values that we would analyse and that can screw the memoisation
# And to resolve that we just make two separate arrays 
#
# To set up the ranges we can just remove an element based on whether 
# We pick the first element or the the last element and thus remove the opposite from the array
# And then perform our search across that such that its like your doing two runs of the algorithm
def rob(nums) -> int:
    
    # Edge case where its not caught during the algorithm so we shall catch it here
    if len(nums) == 1:
        return nums[0]
    
    memo1 = [-1] * len(nums)
    memo2 = [-1] * len(nums)
    def step(nums, index, memo):

        if index < 0:
            return 0
        if memo[index] >= 0:
            return memo[index]
        
        result = max(step(nums, index - 2, memo) + nums[index], step(nums, index - 1, memo))
        memo[index] = result
        return result
    
    return max(step(nums[:-1], len(nums[:-1]) - 1, memo1), step(nums[1:], len(nums[1:]) - 1, memo2))

# ========== Solution 2 ========== #
# As similar as above but instead we store it through variables 
# And remember to split the bounds up with the array splicing
# Note that splicing probably is O(n) so we can pass the bounds in if we wanted to improve time complexity
def rob(nums) -> int:
    if len(nums) == 1:
            return nums[0]
        
    def step(nums):
        first = 0
        second = 0

        for number in nums:
            temp = max(first + number, second)
            first = second
            second = temp
        return second
        
    return max(step(nums[:-1]), step(nums[1:]))