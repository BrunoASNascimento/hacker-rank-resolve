# Enter your code here. Read input from STDIN. Print output to STDOUT
p = input().split(' ')
n = int(input())

p = float(p[0])/float(p[1])

finaly = 0

for i in range(1, n+1):
    finaly += ((1-p)**(i-1))*p

print(round(finaly, 3))
