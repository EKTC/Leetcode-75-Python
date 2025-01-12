import string

class Solution:
    
    # ============== Solution 1 ================== #
    # Loops through the characters of the string and checks if they are alphanumeric
    # If they are add it to the new_string variable
    # Once fully traversed compare the string and its reverse
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        
        for character in s:
            if character.isalnum():
                new_string += character.lower()
            
        return new_string == new_string[::-1]
    
    # ============== Solution 2 ================== #
    # The two pointers solution 
    # The pointers are moved till they reach an alpha numeric character
    # We then check if they match as they are on opposite ends
    # Continue till the entire string is checked or if there is a mismatch
    def isPalindromeV2(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            
            # These two inner loops help shift the pointers
            # We also need the "l < r" check to ensure the index is still valid
            while not s[l].isalnum() and l < r:
                l += 1
            
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l +=1 
            r -=1 

        return True
    
    # ============== Solution 3 ================== #
    # This is a more tuned solution
    # I believe i thought of this with the help of finding how to remove all punctuation
    # " str.maketrans('', '', string.punctuation) " -> Basically states to remove all punctuation or make it None
    # And then the " s.translate " is the actual targeting of the string we want to translate / map to
    # We then join the characters make it lower and do our reverse comparison again
    def isPalindromeV3(self, s: str) -> bool:
        s_final = s.translate(str.maketrans('', '', string.punctuation))
        s_final = "".join(s_final.split()) 
        s_final = s_final.lower() 
        return s_final == s_final[::-1]

    # ============== Solution 4 ================== #
    # Uses regex instead to filter
    def isPalindromeV4(self, s: str) -> bool:
        import re

        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s1 = s1.lower()
        return s1 == s1[::-1]
