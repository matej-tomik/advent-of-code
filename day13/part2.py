def reflection(matrix_i: list[str]) -> int:
    for col in range(1, len(matrix_i[0])):
        split = min(col, len(matrix_i[0]) - col)
        num_differences = 0
        for row in matrix_i:
            for l, r in zip(row[col - split:col], row[col:col + split][::-1]):
                if l != r:
                    num_differences += 1
            if num_differences > 1:
                break
        if num_differences == 1:
            return col


def matrix_rot90(matrix_i: list[str]):
    return [''.join(matrix_i[y][x] for y in range(len(matrix_i))) for x in range(len(matrix_i[0]))]


q = open('data.txt', 'r').read().strip()
data_set = [x.split('\n') for x in q.split('\n\n')]
total = 0
for matrix in data_set:
    row = reflection(matrix_rot90(matrix))
    col = reflection(matrix)
    try:
        total += row * 100
    except:
        total += col
print(total)

