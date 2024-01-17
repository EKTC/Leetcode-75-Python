# ========= Solution 1 =========== #
# This method is where we have a variable current_reach which tracks how far we can go
# We loop through the array of nums whilst checking that our reach can go past the current index
# Otherwise it means we cannot go any further and return False
# We then check if the new index gives us more reach or not and update it accordingly
def canJump(nums) -> bool:
    current_reach = 0
    for index, n in enumerate(nums):
        if current_reach < index:
            return False
        
        current_reach = max(current_reach, n + index)
    
    return True

# ========= Solution 2 =========== #
# This solution is where we constantly shift the "goal" variable to a new index if that index can reach it
# We do this as if we can reach that index then we can reach the end and it will be True for the scenario
# If the "goal" is not at 0 that means we have cannot reach the end and its False
def canJump(nums) -> bool:
    goal = len(nums) - 1 

    # Looping backwards and checking if the index can reach the goal
    # And updating the variable accordingly
    for index in range(len(nums) - 1, -1, -1):
        if index + nums[index] >= goal:
            goal = index
        
    if goal == 0:
        return True
    else:
        return False

# ========= Solution 3 =========== #
# This solution is a standard DP layout
# The idea is that we have an array initialised all to False and if we can reach an index from a previous index
# We would then mark it as True, meaning we can reach that node thus for subsequent revisits of that index we can immediately continue
# Though in practice we do only save a little bit of time as theres not much calculations 
# We continue going and then check the last index and if True it means we have been able to reach the last index
def canJump(nums) -> bool:
    array_length = len(nums) 

    # Base case of just having one element
    if array_length == 1:
        return True

    # Initialising the array to hold our previous values 
    # Also setting a base case to allow for the algorithm to work
    dp = [False] * array_length
    dp[0] = True

    
    for index, n in enumerate(nums):
        max_bound = index + n
        
        # Case to deal with if we are at the end
        # We should break early as it is not really involved in the process
        # As this index should be changed based on other indices
        if index == array_length - 1:
            break
        
        # Loop within the bound of the index and the max_bound which is the amount of steps possible
        for inner_bound in range(index, max_bound + 1):
            
            # Case to deal with ranges that overextend the maximum so we just break early here 
            if inner_bound >= array_length:
                break
            # If its already in the dp array we just continue and dont have to reassign it
            elif dp[inner_bound]:
                continue
            # If the index is True and reachable we can then declare all the indicies within its range True and able to jump to
            elif dp[index]:
                dp[inner_bound] = True

    return dp[array_length - 1]