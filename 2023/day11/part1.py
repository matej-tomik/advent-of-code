def add_extra_row_col(matrix):
    rows, cols = len(matrix), len(matrix[0])
    added = False
    for i in range(rows):
        if added:
            added = not added
            continue
        if all(cell == '.' for cell in matrix[i]):
            matrix.insert(i+1, ['.'] * cols)
            rows += 1
            added = not added

    added = False
    for j in range(cols):
        if added:
            added = not added
            continue
        if all(matrix[i][j] == '.' for i in range(rows)):
            for i in range(rows):
                matrix[i].insert(j + 1, '.')
            cols += 1
            added = not added

    return matrix


def find_galaxies(matrix):
    coordinations = []
    for rows_count,rows in enumerate(matrix):
        for character_count, character in enumerate(rows):
            if character == '#':
                coordinations.append((rows_count,character_count))

    return coordinations

q = open('data.txt', 'r').read().strip('\n')
distance_of_galaxy = find_galaxies(add_extra_row_col([[*x] for x in q.split('\n')]))
total = 0
for count, distance_a in enumerate(distance_of_galaxy):
    for distance_b in distance_of_galaxy[count:]:
        total += abs(distance_b[0] - distance_a[0]) + abs(distance_b[1] - distance_a[1])
print(total)

