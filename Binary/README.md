# 371. Sum of Two Integers

Link: https://leetcode.com/problems/sum-of-two-integers/

- Recognise that its about bits and we can add bits together with XOR
- To determine the carry bits we use AND and shift it over by 1
- Constantly do it till the carry is 0 meaning theres no more modifications

# 191. Number of 1 Bits

Link: https://leetcode.com/problems/number-of-1-bits/

- Brian-Kerninghan's Algorithm to find rightmost bits quicker
- Or you can brute force it and check every bit to see if its set or not

# 338. Counting Bits

Link: https://leetcode.com/problems/counting-bits/

- Use of dynamic programming to reuse values as there is a pattern based on the number of set bits based on the powers of 2
- Another method detailed here https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/
