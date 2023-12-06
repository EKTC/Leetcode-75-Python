def getSum(a, b):
    
    # bits in python are weird
    # For this post here https://leetcode.com/problems/sum-of-two-integers/solutions/489210/read-this-if-you-want-to-learn-about-masks/
    # perfectly encapsulates the difficulties with binary in python
    
    # We use a mask to limit the number of bits python shows to only 32
    # Python has a thing where it does not limit the number of bits
    # to just 32 and it has a wider range
    # The extra carry bit is normally ignored but here
    # it contiually adds on so it loops
    mask = 0xffffffff
    
    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    
    # needs another check at the end as negative numbers will cause a loop
    return (a & mask) if b > 0 else a
        
if __name__ == "__main__":
    print(getSum(1, 2))