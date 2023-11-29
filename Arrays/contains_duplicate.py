def containsDuplicate(nums):
    
    # Adds all numbers to a set 
    # If we see the number in the set and its the current numbner
    # We can terminate and return true, if we loop through
    # The entire list and do not see a duplicate return false
    seen = set()
    
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    
    return False
    
    
if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))