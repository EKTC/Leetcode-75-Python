# ============= Solution 1 ========== #
# Two pointers solution
# Similar to the code of longest palindrome for both solutions
# To run it back
# This solution aims to choose a center base on the index of the string
# And as a result we expand the center to include more letters and checking if its a palindrome
# If it is then we can continue otherwise end our search
# Two cases an odd and an even case which we have to account for that has been broken down into two separate loops
def countSubstrings(self, s: str) -> int:
    count = 0

    for index in range(len(s)):
        left = index
        right = index

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    for index in range(len(s)):
        left = index
        right = index + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count

# ============= Solution 2 ========== #
# Bottom Up DP solution 
# Idea is that we have a DP array that marks all the palindromes and 
# We start from the end of the string and slowly add more characters and using our previous results to check if the new string is a palindrome
# If the two new letters added are equal and the inner substring are palindromes then that means the new string we have is also a palindrome
def countSubstrings(self, s: str) -> int:
        
        count = 0
    
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        
        for left in range(len(s) -1, -1, -1):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    if (right - left) == 1 or dp[left + 1][right - 1] == True:
                        dp[left][right] = True
                        count += 1
        
        return count