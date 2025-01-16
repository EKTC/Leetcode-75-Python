'''
With this question we first do smth kinda nice which is
1) Reverse the strings so we can add them in the way a computer would (mmm thought abt this very nice)
2) The next step is to then do the addition and keep track of the carry bits
3) We also need to make sure to recalculate if theres a carry
'''
def addBinary(self, a: str, b: str) -> str:
    carry = 0
    final = ""
    a = a[::-1]
    b = b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0

        # Total is for helping calculate if we need the carry
        total = digitA + digitB + carry
        char = str(total % 2)
        final = char + final
        carry = total // 2
    
    if carry:
        final = "1" + final
    
    return final
    