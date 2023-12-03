def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid

        # We want to check whether the mid is part of the left or right
        # The first check here is the mid being part of the left hence left sorted
        if nums[mid] >= nums[left]:
            # Inside here we have to check on two conditions to determine whether we search on the left or right
            # If the target is bigger than the middle number that means its on the right
            # Or if the target is smaller than the left most number that means it is on the right as it wraps around
            # Hence we need to search in the right section
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
                
            
    return -1



if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))