# 3. Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

- Sort of a sliding window where if we see a dupe we shift the window till that dupe is gone
- We can keep track of seen characters with a set / array
- Cool solution that uses a dictionary instead to keep track that means we do not need another loop :D

# 5. Longest Palindromic Substring

Link: https://leetcode.com/problems/longest-palindromic-substring/description/

- First method is to use two pointers
- Choose a starting letter and expand left and right checking if its a valid palindrome, do so with every letter
- Note for this there is an odd and even case we have to deal with
- Second approach is a Bottom Up DP method where we fill out our DP table from bottom to top and check if the previous combinations are palindromes to check if our current substring is one
- Both approaches are `O(n^2)` time

# 20. Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses/

- Have a dictionary / hashmap to determine if its a closing brace to allow us to find its corresponding open brace
- Popping off the elements to slowly reduce the amount of parentheses to manage as we find pairs
- Loop through till the entire stack is matched thus meaning its possible else its false

# 49. Group Anagrams

Link: https://leetcode.com/problems/group-anagrams/

- An approach that is `m * nlog(n)` or a faster `m * n * 26` approach
- Slower and first approach is to sort each string and sort them based on this
- Other approach is to track how many occurences of characters are in each string and use that as the key to sort them off

# 76. Minimum Window Substring

Link: https://leetcode.com/problems/minimum-window-substring/description/

- Two pointers setup for a sliding window
- Have a hashmap / dict to track all the needed letters and their frequencies
- Have a hashmap / dict to track all the needed letters and current frequencies within the window
- Have a variable that helps track when all needed letters are fulfilled and the current window is valid
- Minimise the window on the left stide till we have to find needed letters again an attempt to find the minimum window

# 125. Valid Palindrome

Link: https://leetcode.com/problems/valid-palindrome/

- Two main solutions, one where you remove all the non alphanumeric characters and then change all characters to lower and finally compare the string and its reverse
- The other solution is to use two pointers in which we have a left and right pointer than goes till they are both an alphanumeric character and checks till the string is
  fully traversed

# 242. Valid Anagram

Link: https://leetcode.com/problems/valid-anagram/

- Two methods
- First method is just to sort the string with sorted and that allows you to compare the strings easily
- Second method is to add each letter from the strings into their respective dictionaries and compare them later

# 383. Ransom Note

Link: https://leetcode.com/problems/ransom-note/description/

- The idea is to grab the count of the letters and compare them to see if possible
- This file has 2 different methods with similar time complexities

# 424. Longest Repeating Character Replacement

Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

- The method is to have a dictionary / hashmap that stores the count of letters that occur in the sliding window
- If you have less elements that can be replaced than the given `k` variable then we can add the total window length as our longest string
- If we realise that we cannot have replace the elements then we shift our window forward as we represent the window with TWO POINTERS
- This results in a O(26 \* n) => O(n)
- The second method which is similar to the first but optimised to just O(n) straight out uses an extra variable
- This extra variable helps us keep track of the frequency of the most occurring character we need to get a higher length of string

# 647. Palindromic Substrings

Link: https://leetcode.com/problems/palindromic-substrings/description/

- This question is very very similar to the question longest palindromic strings BUT instead of finding the longest string we try to find the number of palindromes
- All the same techniques work as we are always just filtering through palindromes in the other question
