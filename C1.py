def ohms_current(v, r):
    current = v / r
    return current
def power_dissipated(i, r):
    power = (i **2) * r  
    return power
v = 12
r = 6
calculated_current = ohms_current(v , r)
calculated_power = power_dissipated(calculated_current, r)
print("Current =", calculated_current, "A")
print("Power =", calculated_power, "W")
