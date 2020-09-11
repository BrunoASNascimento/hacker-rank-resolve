# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

lambda_num = float(input())
k = float(input())
p = ((lambda_num**k)*(math.e**(-lambda_num)))/(math.factorial(k))

print(round(p, 3))
