Question = int(input("How many resistors are connected in series?:"))
Rtotal = 0
for i in range(Question):
    R = float(input("Enter R in ohms: "))
    Rtotal = Rtotal+R
    i = i + 1
print("Total Resistance:", Rtotal)
    
   
