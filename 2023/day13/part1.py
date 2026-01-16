def reflection(matrix_i: list[str]) -> int:
    for col in range(1, len(matrix_i[0])):
        spit = min(col, len(matrix_i[0]) - col)
        reflection = True
        for row in matrix_i:
            if row[col - spit:col] != row[col:col + spit][::-1]:
                reflection = not reflection
                break
        if reflection:
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
