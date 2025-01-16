"""
    The first solution first gets all the unique letters to compare
    And then gets the count of them and compares if its possible
"""
def canConstructV1(self, ransomNote: str, magazine: str) -> bool:
        unique_letters = list(set(ransomNote))
        for letter in unique_letters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False;
            
        return True;
""" 
    The second solution follows the same logic but uses Counter from a collections import
    To optimise the sorting and gathering of items for comparison
"""
def canConstructV2(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransomCount = Counter(ransomNote)
        magCount = Counter(magazine)
      
        for key in ransomCount:
            # Basically this conidition says we 
            # hey its in the ransomNote but not in the magazine so we can 
            # never construct the word
            if not magCount[key]:
                return False
            
            if magCount[key] < ransomCount[key]:
                return False
        
        return True
