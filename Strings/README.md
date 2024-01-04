# 3. Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

- Sort of a sliding window where if we see a dupe we shift the window till that dupe is gone
- We can keep track of seen characters with a set / array
- Cool solution that uses a dictionary instead to keep track that means we do not need another loop :D

# 20. Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses/

- Have a dictionary / hashmap to determine if its a closing brace to allow us to find its corresponding open brace
- Loop through till the entire stack is matched thus meaning its possible else its false

# 49. Group Anagrams

Link: https://leetcode.com/problems/group-anagrams/

- An approach that is `m * nlog(n)` or a faster `m * n * 26` approach
- Slower and first approach is to sort each string and sort them based on this
- Other approach is to track how many occurences of characters are in each string and use that as the key to sort them off

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
