from collections import defaultdict

class Solution:
    # ================= Solution 1 ====================== #
    # This is the slower solution but its something that is more reasonable to think of as a first solution
    # The idea is that you add the words based on its sorted string which is the key of the dicitonary
    # And append them into their respective lists
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_keys = {}

        for word in strs:
            key = sorted(word)
            key = "".join(key)
    
            if key not in str_keys:
                str_keys[key] = [word]
            else:
                str_keys[key].append(word)
        
        return list(str_keys.values())

    # ================= Solution 2 ====================== #
    # This is a faster solution in terms of time complexity
    # If we are given the word "eat" we would store its key based on it having one "e", one "a" and one "t"
    # And then add all the words that have the same word count
    # This would be faster as we involve the alphabet of lower case letters which is 26 and having to search them through once
    # Rather than relying on a sorting algorithm which at best is nlogn
    def groupAnagramsV2(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Allows mapping of keys that dont exist by not throwing out a keyError and having a default value assigned which here is an empty lsit

        for s in strs:

            # Intialise our array where index 0 will hold how many "a" letters there are in the word etc etc 
            count = [0] * 26 
            for character in s:
                # Using the ascii value representation to calculate the indexes
                count[ord(character) - ord("a")] += 1
            
            result[tuple(count)].append(s) # Remember that lists do not work as keys due to them being mutable so use a tuple :)
        
        return result.values()