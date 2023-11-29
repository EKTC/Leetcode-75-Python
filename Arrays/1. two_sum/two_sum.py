def twoSum(nums, target):
    seen = {}
    # Loop through the values and track the index
    for ind, n in enumerate(nums):
        result = target - n
        
        # Means we have a valid combination for the target and return the indexs
        if result in seen:
            return [seen[result], ind]
        
        # Otherwise insert into the dictionary with the index
        seen[n] = ind
        
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))