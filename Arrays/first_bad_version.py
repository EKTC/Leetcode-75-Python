# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # So if its false it means its later versions
        # If its true we want to check back for earlier versions to check

        # Those were my initial thoughts but we want it to be faster
        # So we do similar stuff to binary search but we know that once theres a bad version all others are bad
        # So if we think about it
        # G G B B B B B
        # We would start at index 0 for left and index 6 for right
        # Our midpoint would be 3
        # So we check move our pointer to index 3 which is bad
        #
        # G G B B B B B
        # L     M     R
        #
        # now we know that its a bad version and we can then say oh what if theres more bad version 
        # BUT WE want the earliest bad version so we can just ignore the later ones hence we move the right pointer up
        # And on the contrast if we have it not being a bad version we can move it up to the midpoint and then + 1 which would jsut decrease the search range
        # its alot faster as we are skipping as we have the required context to do so safely and is needed to pass the time constraints
        # 
        # Then at the since we know the left has moved up to the bad version we can jsut return that
        
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid # leftmost bad version
            else:
                l = mid + 1 # One after the rightmsot good one

        return l