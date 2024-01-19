# ============ Solution  ============== #
# The idea of this is to have a sliding window
# But not only having a sliding window but having alot of other variables to keep track of necessary information
#
# The information we need to collect is:
# @ needed_letters => a dictionary / hashmap of all the letters the window needs to have
# @ window_letters => dictionary / hashmap that will hold the current letters we have in the window
# @ start => the starting index of the final string 
# @ end => the ending index of the final string
# @ matches => the amount of unique letters we have accounted for already in the `needed_letters`
# 
# With this in mind we will slowly move our window and check if there is a valid letter to be added
# If it is a valid letter we can then check if it fulfills the requirements of needed_letters, if so `matches` gets incremented
# When the `matches` equals the length of the unique letters in `needed_letters` we can then start reducing our window in attempt to finding a smaller range
# This solution is at worse an O(n^2) solution due to the two for loops
def minWindow(s: str, t: str) -> str:
    
    # Edge Cases
    if len(t) == 0 or len(t) > len(s):
        return ""
    
    # We want to track the amount of letters we need to have in our window
    needed_letters = {}
    for t_letter in t:
        needed_letters[t_letter] = needed_letters.get(t_letter, 0) + 1
    
    # Holds the letters currently in the window
    window_letters = {}

    # Variables to hold the indicies for the overall minimum window answer
    # Make this large such that its guarantee to switch on the first full match
    start = 0
    end = float(inf)

    # Matches variable to check if we satisfied the condition rather than have to check the hashmap each time
    # This will save alot of time
    matches = 0
    left = 0
    for right in range(len(s)):
        # Checks if the letter is something we need to care about otherwise we can just ignore
        if s[right] in needed_letters:
            window_letters[s[right]] = window_letters.get(s[right], 0) + 1

            # If the number of letters we need is fulfilled we can increase the matches variable
            if window_letters[s[right]] == needed_letters[s[right]]:
                matches += 1
            
            # If we have all the letters we need 
            # We can now start update our indicies which we will use to get the result string after the loop
            # And whilst doing that we will shrink the window in attempt to find the minimum 
            while matches == len(needed_letters):
                # Our condition to check if the new indicies are smaller than our current minimum
                # Note we will do right + 1 as to help with the slicing at the end
                if (end - start) > (right - left):
                    start = left 
                    end = right + 1

                # Checking if we can remove the letter and if the condition of letters we need has now been nullified 
                if s[left] in needed_letters:
                    window_letters[s[left]] -= 1
                    if window_letters[s[left]] < needed_letters[s[left]]:
                        matches -= 1
                    
                left += 1
    
    # Edge case of single word strings resulting in an empty string result
    if end == float(inf):
        return ""

    return s[start:end]