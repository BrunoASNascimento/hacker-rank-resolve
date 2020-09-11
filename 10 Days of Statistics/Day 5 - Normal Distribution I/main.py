import math

mean, sd = map(float, input().split())
x = float(input())
y1, y2 = map(float, input().split())


def normal_distribution(x, mean, sd):
    return (0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))))


print(round(normal_distribution(x, mean, sd), 3))
print(round(normal_distribution(y2, mean, sd)-normal_distribution(y1, mean, sd), 3))
