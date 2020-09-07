# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

value_0 = input()
value_1 = input()

value = [float(x) for x in value_1.split(' ')]

print(np.mean(value))  # Mean
print(np.median(value))  # Median
print(np.bincount(value).argmax())  # Mode
