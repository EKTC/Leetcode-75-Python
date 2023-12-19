def coinChange(coins, amount) -> int:
    # We set up an array that will hold all values
    # from 0 to the amount we are given
    # We set the value to be a value similar to infinity
    # So we can set a changed value below
    dp = [amount + 1] * (amount + 1)
    
    # This is our base case and we need to set this
    # Otherwise the algorithm does not work
    dp[0] = 0
    
    # Loop through all the possible amounts
    for index in range(1, amount + 1):
        # Now loop through the coins to test all the combinations
        # To make the specified amount
        for c in coins:
            # This gets the other value we will use based on the current coin
            # eg: If the index is currently 3 and the coin we are using is 1
            # This gives us remainder of 2 so we would look up dp[2] and use that value
            remainder = index - c
            
            # Means that its a valid combination and we can check it 
            if remainder >= 0:   
                dp[index] = min(dp[index], dp[remainder] + 1)

    # Returns if there was a valid combination or not 
    return dp[amount] if dp[amount] != amount + 1 else -1
    
        
if __name__ == "__main__":
    print(coinChange([1,2,5], 11))
