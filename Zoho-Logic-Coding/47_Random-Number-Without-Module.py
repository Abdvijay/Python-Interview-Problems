import time

def pseudo_random(start, end):
    # Get current time in nanoseconds
    seed = time.time_ns()  
    # Use a simple linear congruential generator formula
    rand = (seed * 9301 + 49297) % 233280
    # Scale the result to desired range
    return start + (rand % (end - start + 1))

print(pseudo_random(100000, 999999))