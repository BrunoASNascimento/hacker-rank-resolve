len_list = int(input())
values = input()
weighted = input()

values_list = [float(x) for x in values.split(' ')]
weighted_list = [float(x) for x in weighted.split(' ')]

calculo = (sum([values_list[i]*weighted_list[i]
                for i in range(0, len_list)])/sum(weighted_list))

print(round(calculo, 1))
