class Solution:
    
    # Solution 1:
    # Return the two as sorted strings for comparison if they are equal then its true otherwise not
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagramV2(self, s: str, t: str) -> bool:
        
        # Edge case to catch if the strings are not equal they will never be able to be anagrams
        if len(s) != len(t):
            return False
            
        s_letters = {}
        t_letters = {}

        # Loop through both strings at the same time
        # Adding the character count for each
        for s_char, t_char in zip(s,t):
            if s_char not in s_letters: 
                s_letters[s_char] = 1
            else:
                s_letters[s_char] += 1

            if t_char not in t_letters:
                t_letters[t_char] = 1
            else:
                t_letters[t_char] += 1
        
        # Loop through the letters of one word
        # Using "get" here as that accounts for when a word is only existing in one dictionary
        # And not the other so we can still do proper comparisons
        for char in s_letters:
            if s_letters[char] != t_letters.get(char, 0):
                return False

        return True