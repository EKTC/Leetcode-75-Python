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
    
        
if __name__ == "__main__":
    print(climbStairs(5))
