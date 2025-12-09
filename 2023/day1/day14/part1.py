f = open('data.txt').read().strip().split('\n')
matrix = [list(m.strip()) for m in f]
total = 0
for x in range(len(matrix[0])):
    position = []
    for y in range(len(matrix) - 1, -1, -1):
        if matrix[y][x] == 'O':
            position.append(y)
        if matrix[y][x] == '#' and len(position) > 0:
            total += len(position) * (len(matrix) - y)
            for tmp in range(1,len(position)+1):
                total -= tmp
            position.clear()
    for tmp in range(len(position)):
        total += len(matrix) - tmp
print(total)