# Enter your code here. Read input from STDIN. Print output to STDOUT
p = input().split(' ')
n = float(input())

p = float(p[0])/float(p[1])

print(round(((1-p)**(n-1))*p, 3))
