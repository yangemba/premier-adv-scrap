list_old = [
    ['18-24', '1381'],
    ['25-34', '3721'],
    ['35-44', '1253'],
    ['45-54', '391'],
    ['55-64', '121'],
    ['65+', '31']
]

total = 0
for el in list_old:
    total += int(el[1])
print(total)

# list_new = [{x[0]: round((int(x[1]) / total) * 100, 2)} for x in list_old]
list_new = [dict(zip(x[0], ((int(x[1]) * 100) / total))) for x in list_old]
print(list_new)