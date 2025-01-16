# The whole point is to reuse values that we have already precalculated so we do not have to recurse any further
# So we use cached values and add onto it as we go
# We return memo[n] as thats the number of ways which we want to find
def climbStairs(n):
    # How this works is that you can only go 1 or 2
    # So you have to recursively call the function
    # You store the data in a dict
    def climb(n): 
        print("Num" + str(n))
        # If we already have calculated the values of it we just return it
        if n in memo:
            return memo[n]
        # Otherwise check the two variations of 1 or 2 steps and store it as 
        # That value for that step
        else:
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

    memo = {1: 1, 2: 2}  # base cases
    return climb(n)
    
# The more naive approach that takes a lot longer
# Simple base cases with the recursive step
def climbStairsV2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    print(climbStairs(5))
