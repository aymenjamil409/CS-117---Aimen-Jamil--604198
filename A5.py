ris1 = float(input("Enter the value of the 1st resistor (in Ω):"))
ris2 = float(input("Enter the value of the second resistor (in Ω):"))
ris3 = float(input("Enter the value of the third resistor (in Ω):"))
if ris1 >= ris2 and ris1 >= ris3:
    largest = ris1
elif ris2 >= ris1 and ris2 >= ris3:
    largest = ris2
else:
    largest = ris3
if ris1 <= ris2 and ris1 <= ris3:
    smallest = ris1
elif ris2 <= ris1 and ris2 <= ris3:
    smallest = ris2
else:
    smallest = ris3
print("Smallest resistor:" , smallest ,"Ω")
print("Largest resistor:" ,largest,"Ω")

