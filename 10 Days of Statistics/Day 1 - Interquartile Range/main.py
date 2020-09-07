# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

len_value = int(input())
element_list = input().split(' ')
frequency_list = input().split(' ')


def calcule_quantile(len_value, value_list):
    value_list = sorted(value_list, reverse=False)
    if len_value % 2 == 0:
        len_value_1 = len_value//2-1
        len_value_3 = len_value//2+1
        q_1 = (float(round(statistics.median(value_list[1:len_value_1]))))
        q_2 = (float(round(statistics.median(value_list))))
        q_3 = (
            float(round(statistics.median(value_list[len_value_3:len_value-1]))))
    else:
        len_value_1, len_value_3 = len_value//2, len_value//2+1
        q_1 = (float(round(statistics.median(value_list[:len_value_1]))))
        q_2 = (float(round(statistics.median(value_list))))
        q_3 = (float(round(statistics.median(value_list[len_value_3:]))))
    return q_1, q_2, q_3


frequency_list = [int(x) for x in frequency_list]
element_list = [float(i) for i in element_list]
finaly = []

for i in range(0, len_value):
    finaly.extend([element_list[i]]*frequency_list[i])

q_1, q_2, q_3 = calcule_quantile(len(finaly), finaly)
print(q_3-q_1)
