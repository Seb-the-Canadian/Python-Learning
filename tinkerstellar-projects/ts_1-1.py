# ts_1-1.py

# Set the midpoint:
midpoint = 5

# Make two empty lists:
lower = []
upper = []

# Split the numbers into lower and upper:
for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)

print("lower:", lower)
print("upper:", upper)
