# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

len_value = int(input())
value_list = input().split(' ')
value_list = sorted([float(x) for x in value_list], reverse=False)

# print(len_value,value_list)

if len_value % 2 == 0:
    len_value_1 = len_value//2-1
    len_value_3 = len_value//2+1
    print(int(round(statistics.median(value_list[1:len_value_1]))))
    print(int(round(statistics.median(value_list))))
    print(int(round(statistics.median(value_list[len_value_3:len_value-1]))))

else:
    len_value_1, len_value_3 = len_value//2, len_value//2+1
    print(int(round(statistics.median(value_list[:len_value_1]))))
    print(int(round(statistics.median(value_list))))
    print(int(round(statistics.median(value_list[len_value_3:]))))
