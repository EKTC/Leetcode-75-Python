from collections import defaultdict

'''
Two solutions here
The first one uses a hashmap style to count the occurences
We only add if its an even occurence to our count
And finally after we check if their are any odd values left which we can add

The theory is that any pair of elements can make a pair and can add onto a palindrome easily
And yu can slot in a pair or a single letter in the middle to complete that palindrome
So thats why we search for pairs and add them as we can guarantee they form a palindrome
'''
def longestPalindromeV1(self, s: str) -> int:
    count = defaultdict(int)
    res = 0
    
    for c in s:
        count[c] += 1
        if count[c] % 2 == 0:
            res += 2
        
    for cnt in count.values():
        if cnt % 2:
            res += 1
    
    return res

'''
This solution is more cleaner one using a set instead
The idea is quite nice where we add it to a set
And when we have seen it twice we can increment and remove it from the set
As we always do something with the pair
Very nice
'''
def longestPalindromeV2(self, s: str) -> int:
    visited = set()
    l = 0

    for ch in s:
        if ch not in visited:
            visited.add(ch)
        else:
            l += 2
            visited.remove(ch)

    if len(visited) > 0:
        l += 1
    
    return l