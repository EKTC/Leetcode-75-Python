'''
    Two similar variations of the same logic
    The idea was to get all the unique elements and checking if
    They are  the majority element
    The first solution is much cleaner than the one below
'''
def majorityElement(self, nums: List[int]) -> int:
        
    # Use a set to get the unique numbers of 
    # Check the counts to be the majority
    # Which is stated as n / 2
    for i in set(nums):
        if nums.count(i) > (len(nums) // 2):
            return i

def majorityElement(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0
        rcount = 0
        for u in unique:
            if rcount < nums.count(u):
                res = u
                rcount = nums.count(u)
        
        return res