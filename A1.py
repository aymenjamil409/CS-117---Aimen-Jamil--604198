V= float(input("Enter the Voltage:"))
R = float(input("Enter the resistance:"))
if R==0 or R<0:
    print("Invalid resistance")
I = V/R
if I>2 :
    print("Fuse will blow")
else:
    print("Circuit is Safe")
