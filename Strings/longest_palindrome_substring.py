# ========= Solution 1 ============= #
# This uses two pointers where the idea is that we get a letter and expand left and right
# We check if its a valid palindrome and if it is we can keep expanding till we reach the bounds
# There are two cases: 
# 1) Odd case
# 2) Even case
#
# Thus we have to check two times for each case, for the code below I just broke it up into two for loops
# For easier readability but they can be condensed if needed
# Time complexity is n^2 due to the 2 loops
def longestPalindrome(self, s: str) -> str:

    result_str = ""
    result_len = 0

    # Odd Case
    for index in range(len(s)):
        left = index
        right = index

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > result_len:
                result_len = right - left + 1
                result_str = s[left:right + 1]

            left -= 1
            right += 1
    
    # Even Case
    # Here we have to grab both indexes as the odd case only accounts that our start is one letter
    for index in range(len(s)):
        left_index = index
        right_index = index + 1
    
        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            if (right_index - left_index + 1) > result_len:
                result_len = right_index - left_index + 1
                result_str = s[left_index:right_index + 1]

            left_index -= 1
            right_index += 1

    return result_str
    
# ========= Solution 2 ============= #
# This uses DP to store the results of previous strings and uses them to check substrings are palindromes
# The DP is a bottom UP approach as we start from the bottom of the table and go up
# When we check a string "ababa" is a palindrome we would check "bab" and then "a" and if they all are palindromes then that means "ababa" is one
# The DP comes is as we have already checked the smaller strings before reaching this larger string meaning we can just check the previous start of the string "bab" 
# To see if that is also True 
# Time complexity and space complexity is n^2 here
def longestPalindrome(self, s: str) -> str:
    current = ""
    
    # This creates an array of arrays that are filled with zeroes 
    # We then set the diagonals to be True, as its our base case
    # But also because a single letter on its own is a palindrome
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        current = s[i]

    # Iterate backwards
    for left in range(len(s) - 1, -1, -1):
        # Set the range to be the bound of the string and the left value
        # We plus one so that we dont get values that can go out of bounds in the checks below
        for right in range(left + 1, len(s)):
            if s[left] == s[right]:
                # Conditions of either
                # 1) There is only one letter in the substring meaning its a palindrome
                # 2) Substring is a palindrome
                if right - left == 1 or dp[left + 1][right - 1] == True:
                    dp[left][right] = True
                    if len(current) < len(s[left:right+1]):
                        current = s[left:right+1]

    return current