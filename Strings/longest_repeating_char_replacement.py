# =========== Solution 1 ========== #
# A sliding window but you keep track of the number of elements in the window
# Our window is built with two pointers
# With K we can define the max if the amount we have to replace is small enough
# Otherwise we shift our window forward in hopes of finding a better string
# Time complexity of 26 * n
def characterReplacement(s, k) -> int:
    letter_count = {}
    result = 0
    left = 0

    # Loop till we reach the end of the array
    for right in range(len(s)):
        # Count the new letter into the dict / hashmap
        letter_count[s[right]] = letter_count.get(s[right], 0) + 1

        # The calculation `(right - left + 1)` is done to find the total length of the string
        # We find the letter with the highest frequency which gives us how many characters we need to replace for them to be all the same
        # And base that off `k`
        # If `k` is smaller we got to decrement our count in the dict and shift our left pointer
        while (right - left + 1) - max(letter_count.values()) > k:
            letter_count[s[left]] -= 1
            left += 1
        
        # Compares the max each time to the new string or current result
        result = max(result, right - left + 1)
    return result

# =========== Solution 2 ========== #
# This solution is the more optimised route that is very similar to the initial solution
# The new lines of code add in the `max_frequency` variable and its assignment
# The way this works is we track the most occurring letter each time we add a new letter
# And now we dont have to lookup the dictionary each time rather we just use the variable
# The variable works as it also acts as our ceiling as even if its inaccurate such that 
# `max_frequency = 5` but the string is only 4 letters, the thing is that at one point the max was 5 and we need a frequency of 6
# To get a new max and our string will never beat that until we get that frequency so it allows it to be inaccurate at points
def characterReplacementV2(s, k) -> int:
    letter_count = {}
    result = 0
    left = 0
    max_frequency = 0

    for right in range(len(s)):
        letter_count[s[right]] = letter_count.get(s[right], 0) + 1

        max_frequency = max(max_frequency, letter_count[s[right]])

        while (right - left + 1) - max_frequency  > k:
            letter_count[s[left]] -= 1
            left += 1
        
        result = max(result, right - left + 1)
    return result
