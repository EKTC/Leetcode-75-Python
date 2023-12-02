def findMin(nums):
    final = nums[0]
    left = 0
    right = len(nums) - 1
   
    # We can do a binary search with a pivot point  
    while left <= right:

        # Check if the left most number is the min 
        # If the left is smaller than the right
        if nums[left] < nums[right]:    
            final = min(final, nums[left])

        # Find the mid point and check if that value is the min
        mid = (left + right) // 2
        final = min(final, nums[mid])
        
        # Have an if condition that is based on whether 
        # The value is left sorted or right sorted
        # If the mid is higher that the left the values smaller should be on the right
        # Though there is a case where it loops around hence why we always
        # Check the left to see if its a minimum
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1


    return final


if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))