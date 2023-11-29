def maxProfit(prices):
    # Index for buying
    left = 0 
    # Index for selling
    right = 1 
    max_profit = 0
    
    # Loop till we go through all the prices
    while right < len(prices):
        
        currentProfit = prices[right] - prices[left] 
        
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right
        right += 1

    return max_profit
        

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))