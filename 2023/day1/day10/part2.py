from sys import setrecursionlimit
from collections import defaultdict


def find_valid_moves(grid_if, pos, pipe_map_if, prev_dir=None):
    valid_directions = pipe_map_if[grid_if[pos[1]][pos[0]]]
    valid_moves = []
    for d in valid_directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        new_pipe_piece = grid_if[new_pos[1]][new_pos[0]]
        if 0 <= new_pos[0] < len(grid_if[0]) and 0 <= new_pos[1] < len(grid_if):
            match d:
                case (0, -1) if (0, 1) in pipe_map_if[new_pipe_piece] and prev_dir != (0, 1):
                    valid_moves.append(new_pos)
                case (0, 1) if (0, -1) in pipe_map_if[new_pipe_piece] and prev_dir != (0, -1):
                    valid_moves.append(new_pos)
                case (1, 0) if (-1, 0) in pipe_map_if[new_pipe_piece] and prev_dir != (-1, 0):
                    valid_moves.append(new_pos)
                case (-1, 0) if (1, 0) in pipe_map_if[new_pipe_piece] and prev_dir != (1, 0):
                    valid_moves.append(new_pos)
    return valid_moves


def find_start_char(grid_if, pos, pipe_map_if):
    valid_moves = find_valid_moves(grid_if, pos, pipe_map_if)
    valid_directions = [(x[0] - pos[0], x[1] - pos[1]) for x in valid_moves]
    for k, v in pipe_map_if.items():
        if v == valid_directions:
            return k


def solve(grid_if, pos, pipe_map_if, visited, prev_dir=None):
    move = find_valid_moves(grid_if, pos, pipe_map_if, prev_dir)[0]
    if move == start_pos and len(visited) > 0:
        return visited
    visited.add(move)
    return solve(grid_if, move, pipe_map_if, visited, (move[0]-pos[0], move[1]-pos[1]))


q = open('data.txt', 'r').read().strip()

grid = [[x for x in row] for row in q.strip().split('\n')]
pipe_map = {'|': [(0, -1), (0, 1)], '-': [(1, 0), (-1, 0)],
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)],
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)],
            '.': [], 'S': [(0, -1), (0, 1), (1, 0), (-1, 0)]}

setrecursionlimit(30000)
start_pos = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]
grid[start_pos[1]][start_pos[0]] = find_start_char(grid, start_pos, pipe_map)
visited = solve(grid, start_pos, pipe_map, {start_pos})
contained = set()
for row in range(len(grid)):
    within = False
    for column in range(len(grid[0])):
        if (column, row) in visited:
            if grid[row][column] in ['|', 'L', 'J']:# not F - or 7 because there are top simbols->no tiles between them
                within = not within
        elif within:
            contained.add((column, row))

print(len(contained))


