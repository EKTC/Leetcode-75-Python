def countBits(n):
    dp = [0] * (n + 1)
    offset = 1
    
    # Loop for all values in the range
    for i in range(1, n + 1):
        # Have an offset as the set bits are based of 
        # previous values that we calculate based on the pattern
        # Occurs every power of 2 so we accomodate that with
        # Updating the offset
        if offset * 2 == i:
            offset = i 
        dp[i] = 1 + dp[i - offset]

    return dp
    
        
if __name__ == "__main__":
    print(countBits(2))
