def count_x(g ,empty_cols_i):
    previous_empty_cols = []
    for x in empty_cols_i:
        if x < g:
            previous_empty_cols.append(x)
    return g + len(previous_empty_cols) * 999999


def count_y(g, empty_rows_i):
    previous_empty_row = []
    for x in empty_rows_i:
        if x < g:
            previous_empty_row.append(x)
    return g + len(previous_empty_row) * 999999


def find_empty_rows_cols(galaxies, x, y):
    empty_rows = []
    for y in range(y):
        if not any([y == g[1] for g in galaxies]):
            empty_rows.append(y)
    empty_cols = []
    for x in range(x):
        if not any([x == g[0] for g in galaxies]):
            empty_cols.append(x)
    return empty_rows, empty_cols



def find_galaxies(matrix):
    coordinations = []
    for rows_count,rows in enumerate(matrix):
        for character_count, character in enumerate(rows):
            if character == '#':
                coordinations.append((character_count, rows_count))

    return coordinations


q = open('data.txt', 'r').read().strip('\n')
dataset = [[*x] for x in q.split('\n')]
x = len(dataset[0])
y = len(dataset)
galaxies = find_galaxies(dataset)
empty_rows, empty_cols = find_empty_rows_cols(galaxies, x, y)
distance_of_galaxy = []
for g in galaxies:
    distance_of_galaxy.append((count_x(g[0], empty_cols), count_y(g[1], empty_rows)))

total = 0
for count, distance_a in enumerate(distance_of_galaxy):
    for distance_b in distance_of_galaxy[count:]:
        total += abs(distance_b[0] - distance_a[0]) + abs(distance_b[1] - distance_a[1])
print(total)
