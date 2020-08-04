cars = list(map(int,input().split(' ')))
total_petrol = sum(cars)
total_cars = len(cars)
table_c = total_petrol // 2
table = [[-1 for _ in range(table_c + 1)] for _ in range(total_cars + 1)]
for i in range(total_cars + 1):
    for j in range(table_c + 1):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif cars[i - 1] <= j:
            table[i][j] = max([table[i-1][j],table[i-1][j - cars[i-1]]+cars[i-1]])
        else:
            table[i][j] = table[i-1][j]
excess = total_petrol - 2 * table[total_cars][table_c]
maximum = ((total_petrol - excess) // 2) + excess
print(maximum,end='')