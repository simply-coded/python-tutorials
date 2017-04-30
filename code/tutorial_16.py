# binary counting.
#0 1  2  3   4   5   6   7    8    9   10   11   12
#0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 

a = 5
b = 3

# shifts bits left or right.
#a << b = a * (2 ** b)
print("Shift left operator: 5 << 3 =", a << b)
#a >> b = a // (2 ** b)
print("Shift right operator: 5 >> 3 =", a >> b)

# convert letter to upper or lowercase.
letr = ord('a')
to_upper = 223 # 0b11011111, 0xDF
to_lower = 32  # 0b00100000, 0x20

print("Bitwise and operator: 97 & 223 =", chr( letr & to_upper ))
print("Bitwise or operator: 97 | 32 =", chr(  letr | to_lower ))

# only keep controversal or opposite bits
print("Bitwise xor operator: 5 ^ 3 =", a ^ b)

# invert all the bits (take the one's complement).
print("Bitwise not operator on 5:", ~a)
print("Bitwise not operator on 3:", ~b)
