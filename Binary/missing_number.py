def missingNumber(nums):
    # Basically finding the sum of the current list
    # And finding the sum of the list with the entire range
    # To find the missing number
    return sum(range(len(nums) + 1)) - sum(nums)
    
        
if __name__ == "__main__":
    print(missingNumber([3,0,1]))