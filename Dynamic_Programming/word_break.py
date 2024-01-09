def wordBreak(s, wordDict) -> bool:
    # We arrange an array that is either true or false
    # Where if its in between two True values that means theres a word from the wordDict there
    # Thus thats why we have a base case of the first element being true and adding another element to the initial array
    tracker = [False] * (len(s) + 1)
    tracker[0] = True # Base Case

    # We now setup two for loops
    # One that has the right bound starting skipping the first element as thats our base case
    # And a left one thats within the bounds of the right slowly checking which set of indices work
    #
    # given s = "leetcode" and wordDict = [leet, code]
    # If we were looping through this example we wound keep looping and expanding our bound till we reach
    # The index of 4 and we recognise that bound is "leet" which is a word
    # In addition our left will be at 0 when we do this check which is true 
    # Thus the bound s[0:4] is a valid word and now tracker[4] is set to True and continue on till the end of the string
    # [True, False, False, False , True]
    #
    for right in range(1, len(s) + 1):
        for left in range(right):
            # We check two conditions if theres a True set in the bound of the string and that the bound created 
            # exists in the wordDict
            if tracker[left] and s[left:right] in wordDict:
                tracker[right] = True
                print(left, right)
                print(s[left:right])
                break

    # We return the last index as we expect it to be true for the string to be valid
    return tracker[-1]

