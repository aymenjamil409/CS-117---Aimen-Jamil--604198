t_1= 0
t_5 = 0
t_reject = 0
while True:
    value = float(input("Enter measured resistance in ohms (or 0 to stop): "))
    if value == 0:
        break
    if value >= 99.0 and value <= 101.0:
        t_1 = t_1 + 1
    elif value >= 95.0 and value <= 105.0:
        t_5 = t_5 + 1
    else:
        t_reject = t_reject + 1
print("\n--- Final Bin Counts ---")
print("1% Tolerance Bin:", t_1)
print("5% Tolerance Bin:", t_5)
print("Reject Bin:", t_reject)

