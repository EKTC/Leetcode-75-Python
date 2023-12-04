def threeSum(nums):
    
    # We have it in a set so we can remove dupes easily
    all_sets = set()
    # Sort it so we can do binary search later
    nums.sort()
    
    # The general idea is to have a set value and then with the remaining array
    # Binary search through it to create the combinations
    # Its an extension of two sum where a possible solution of two sum
    # Was to simply sort the array and binary search to get the values that would get the sum
    # As you keep going the array gets smaller with the possible combinations invovled.
    for index, set_num in enumerate(nums):
        
        new_nums = nums[index + 1:]
        left = 0
        right = len(new_nums) - 1
        
        while left < right:
            sum = set_num + new_nums[left] + new_nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0: 
                left += 1
            else: 
                all_sets.add((set_num, new_nums[left], new_nums[right]))
                left += 1
    
    # Final part of code that transforms it into a list for returning 
    final_list = []
    for val in all_sets:
        final_list.append(list(val))
    return final_list
        
if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))