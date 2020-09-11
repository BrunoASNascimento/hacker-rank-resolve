# Enter your code here. Read input from STDIN. Print output to STDOUT
values = input()
values = [float(x) for x in values.split(' ')]

for num in values:
    if num == 0.88:
        c = 160 + 40 * (num+num**2)
    if num == 1.55:
        c = 128 + 40 * (num+num**2)
    print(round(c, 3))
