import math

mean, sd = map(float, input().split())
x, y = float(input()), float(input())


def normal_distribution(x, mean, sd):
    return round(0.5 * 100 * (1 + math.erf((x - mean) / (sd * math.sqrt(2)))), 3)


print(round(100 - normal_distribution(x, mean, sd), 2))
print(round(100 - normal_distribution(y, mean, sd), 2))
print(round(normal_distribution(60, 70, 10), 2))
