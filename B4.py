voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
current_streak = 1
current_start = voltages[0]
max_streak = 1
start = voltages[0]
end = voltages[0]
for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_streak = current_streak + 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
            start = current_start
            end = voltages[i - 1]
            current_streak = 1
            current_start = voltages[i]
        if current_streak > max_streak:
           max_streak = current_streak
           start = current_start
           end = voltages[len(voltages) - 1]
print("Longest continuous drop:", max_streak, "minutes")
print("Started at:", start, "V")
print("Ended at:", end, "V")
