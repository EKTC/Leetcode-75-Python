def maxSubArray(nums):
    # Initialise the sum to be the first element
    maxSum = nums[0]
    # Store our current sum
    curr = 0
    
    for n in nums:
        
        # In the end we do not care about negative sums
        # And hence if we have the chance of a positive sum
        # We can take that 
        if curr < 0:
            curr = 0
            
        curr += n
        # Checks which is larger the new sum or the current max
        maxSum = max(maxSum, curr)
    
    return maxSum
    

    
if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
     