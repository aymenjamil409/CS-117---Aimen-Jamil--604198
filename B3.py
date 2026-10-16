readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
highest = readings[0]
lowest = readings[0]
t_sum = 0
t_count = 0
for voltage in readings:
     if voltage > 3.2:
        count = count + 1
     if voltage > highest:
         highest = voltage
     if voltage < lowest:
         lowest = voltage
     t_sum = t_sum + voltage
     t_count = t_count + 1
average = t_sum / t_count
print("(a) Number of readings above 3.2 V:",count)
print("(b) Highest reading:" ,highest, "V")
print("(c) Lowest reading:" ,lowest ,"V")
print("(d) Average reading:" ,average, "V")
