# 371. Sum of Two Integers

Link: https://leetcode.com/problems/sum-of-two-integers/

- Recognise that its about bits and we can add bits together with XOR
- To determine the carry bits we use AND and shift it over by 1
- Constantly do it till the carry is 0 meaning theres no more modifications
