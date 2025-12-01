start_value = int(input("Enter start value: "))
target_value = int(input("Enter target value: "))
steps = 0

current_value = target_value
step = []
while current_value > start_value:
    if current_value % 2 == 0:
        current_value //= 2
    else:
        current_value += 1
    steps += 1
    step.append(str(current_value))

steps += (start_value - current_value)

print(f"Steps : {"->".join(step)}, Total Steps : {steps}")

# SAMPLE INPUT AND SAMPLE OUTPUT 1
# Enter start value: 2
# Enter target value: 3
# Steps : 4->2, Total Steps : 2

# SAMPLE INPUT AND SAMPLE OUTPUT 2
# Enter start value: 4
# Enter target value: 13
# Steps : 14->7->8->4, Total Steps : 4