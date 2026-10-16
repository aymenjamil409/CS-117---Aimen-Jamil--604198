A = int(input("Enter bit A either 0 or 1: "))
B = int(input("Enter bit B either 0 or 1: "))
if A in (0,1) and (B in (0,1)):
    print("Valid input")
else:
    A = int(input("Enter bit A either 0 or 1: "))
    B = int(input("Enter bit B either 0 or 1: "))
AND_result = A and B
OR_result = A or B
XOR_result = (A and (not B) ) or ((not A) and B)
print("AND:", AND_result)
print("OR:", OR_result)
print("XOR:", XOR_result)
