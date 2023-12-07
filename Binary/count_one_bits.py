def hammingWeight(n):
    
    total = 0
    
    # We have two methods
    # The first method here is a more naive solution
    # Where we just count the number of one bits every time
    # and iterate through all the bits
    while n:
        total += n % 2
        n = n >> 1
    
    # The second solution is based on an algo
    # Such that it always removes the rightmost set bit
    # Hence we count how many times it occurs
    while n:
        n = n & (n - 1)
        total += 1
    return total
    
        
if __name__ == "__main__":
    print(hammingWeight(00000000000000000000000000001011))
