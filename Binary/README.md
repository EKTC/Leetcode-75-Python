# 67. Add Binary

Link: https://leetcode.com/problems/add-binary/description/

- When adding binary bits the main thing is the carry bit when we add two ones
- We need to track and account for that in each of the steps of addition
- And to mock how binary is stored remembered if a string is not long enough we can just pad with zeroes mmm

# 190. Reverse Bits

Link: https://leetcode.com/problems/reverse-bits/

- Set the bits one by one with the new order
- Starting at the far left as we are reversing it

# 191. Number of 1 Bits

Link: https://leetcode.com/problems/number-of-1-bits/

- Brian-Kerninghan's Algorithm to find rightmost bits quicker
- Or you can brute force it and check every bit to see if its set or not

# 268. Missing Number

Link: https://leetcode.com/problems/missing-number/

- Find the sum of the list and sum of the entire range and you will get the difference that gives the missing number
- Can also be done with XOR, as 2 ^ 2 = 0 and then you will be left with the missing number

# 338. Counting Bits

Link: https://leetcode.com/problems/counting-bits/

- Use of dynamic programming to reuse values as there is a pattern based on the number of set bits based on the powers of 2
- Another method detailed here https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/

# 371. Sum of Two Integers

Link: https://leetcode.com/problems/sum-of-two-integers/

- Recognise that its about bits and we can add bits together with XOR
- To determine the carry bits we use AND and shift it over by 1
- Constantly do it till the carry is 0 meaning theres no more modifications
