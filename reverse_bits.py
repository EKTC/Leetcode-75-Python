def reverseBits(n):
    final = 0
    
    for i in range(32):
        # To get the bit if its set or not
        bit = (n >> i) & 1
        
        # As we are reversing it we want the bit
        # To be shifted all the way at the start
        # Using logic OR to maintain the other bits
        final = final | (bit << (31 - i))
    return final
    
        
if __name__ == "__main__":
    print(reverseBits(00000010100101000001111010011100))
