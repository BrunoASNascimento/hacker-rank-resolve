n = input()
ar = input().split(' ')

data = {}
for num_test in ar:
    control = data.get(num_test)
    if control is None:
        data[num_test] = 1
    else:
        data[num_test] += 1

data_finally = 0
for key, value in data.items():
    if value % 2 == 1:
        data_finally += 1

calculo = int(n)-data_finally
print(int(calculo/2))
