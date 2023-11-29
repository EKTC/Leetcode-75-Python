def maxProduct(nums):
    
    # Final Sum
    final_sum = max(nums)
    # Max sum currently
    max_sum = 1
    # Min sum currently
    min_sum = 1
    
    for n in nums:
        # As discussed earlier the 0 resets
        # Rather than set it to 0 which would screw
        # The algorithm set it to 1
        if n == 0:
            max_sum = 1
            min_sum = 1
        
        # We need to store the max_sum somewhere as 
        # We may mutate it below
        # You can make it the min_sum variable and nothing
        # changes
        tmp = max_sum
        
        # We need to check 3 things are max or min
        # 1) n -> the number in the array
        # 2) max_sum * n -> the max sum with the new number
        # 3) min_sum * n -> the min sum with the new number
        max_sum = max(n, max_sum * n, min_sum * n)
        min_sum = min(n, tmp * n, min_sum *n)
        
        final_sum = max(max_sum, final_sum)
        
    return final_sum
            
    

    
if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))
     