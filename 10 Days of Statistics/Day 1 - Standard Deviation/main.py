# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

len_value = int(input())
value_list = input().split(' ')
value_list = sorted([float(x) for x in value_list], reverse=False)

sum_numbers = 0
list_mean = statistics.mean(value_list)

for number in value_list:
    sum_numbers = sum_numbers + (number-list_mean)**2

print(round((sum_numbers/len_value)**(1/2), 1))
