class Solution:
    # First Solution that is much more optimal
    # Store the seen in a dict but instead when we get a dupe just jump
    # To the index and continue on
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        # We take the index and the character each time
        for i, c in enumerate(s):
            # We check if this is already in the string
            # And that the start index we have used to track it is too far away
            # If so we then jump to that index and + 1 to move it over
            # Thus updating our variable to keep track of how much of the string is left
            if c in used and start <= used[c]:
                start = used[c] + 1
            # We plus 1 as its zero indexed and to align the length properly
            # But also in the calculation we get how much of our start index placeholder is compared to where we currently are in
            # The string to get the length
            else:
                max_length = max(max_length, i - start + 1)
            
            # This is just adding the character in to the dict
            # With its key being the char itself
            # Value being the index it is
            used[c] = i

    
        return max_length
    
    # Second approach is much more simpler and straight forward
    # We store all the characters in a set to track when we get a duplicate
    # We have an index variable to track what index we are at
    # So we can remove characters 
    def lengthOfLongestSubstringV2(self, s: str) -> int:
        seen_chars = set()
        biggest_length = 0

        index = 0
        # Checks each character and if the character
        # Exists in the set already we loop and remove them till
        # We have gotten rid of it 
        # We increment the index variable to traverse through the set properly
        for character in s:
            while character in seen_chars:
                seen_chars.remove(s[index])
                index += 1
            
            # Here after the iteration we just add the character
            # And do a check on the length
            seen_chars.add(character)
            biggest_length = max(biggest_length, len(seen_chars))
        
        return biggest_length
