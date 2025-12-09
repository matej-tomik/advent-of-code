def tilt_platform(platform_i, direction):
    if direction == 'north':
        for i in range(len(platform_i)):
            for j in range(len(platform_i[0])):
                if platform_i[i][j] == 'O':
                    for k in range(i-1, -1, -1):
                        if platform_i[k][j] == '#':
                            break
                        elif platform_i[k][j] == '.':
                            platform_i[k][j] = 'O'
                            platform_i[k+1][j] = '.'
                    else:
                        platform_i[0][j] = '.'
    elif direction == 'west':
        for i in range(len(platform_i)):
            for j in range(len(platform_i[0])):
                if platform_i[i][j] == 'O':
                    for k in range(j-1, -1, -1):
                        if platform_i[i][k] == '#':
                            break
                        elif platform_i[i][k] == '.':
                            platform_i[i][k] = 'O'
                            platform_i[i][k+1] = '.'
                    else:
                        platform_i[i][0] = '.'
    elif direction == 'south':
        for i in range(len(platform_i)-1, -1, -1):
            for j in range(len(platform_i[0])):
                if platform_i[i][j] == 'O':
                    for k in range(i+1, len(platform_i)):
                        if platform_i[k][j] == '#':
                            break
                        elif platform_i[k][j] == '.':
                            platform_i[k][j] = 'O'
                            platform_i[k-1][j] = '.'
                    else:
                        platform_i[-1][j] = '.'
    elif direction == 'east':
        for i in range(len(platform_i)):
            for j in range(len(platform_i[0])-1, -1, -1):
                if platform_i[i][j] == 'O':
                    for k in range(j+1, len(platform_i[0])):
                        if platform_i[i][k] == '#':
                            break
                        elif platform_i[i][k] == '.':
                            platform_i[i][k] = 'O'
                            platform_i[i][k-1] = '.'
                    else:
                        platform_i[i][-1] = '.'
    return platform_i


def plat_to_string(platform_i):
    return 'y'.join(['x'.join(x) for x in platform_i])


def string_to_plat(string):
    return [x.split('x') for x in string.split('y')]


input_file = 'data.txt'

f = open(input_file).read().strip()

platform = [['#'] + list(x) + ['#'] for x in f.strip().split('\n')]
platform.insert(0, ['#']*len(platform[0]))
platform.append(['#']*len(platform[0]))
size = len(platform)

stored_states = [plat_to_string(platform)]
while True:
    platform = tilt_platform(platform, 'north')
    platform = tilt_platform(platform, 'west')
    platform = tilt_platform(platform, 'south')
    platform = tilt_platform(platform, 'east')
    if plat_to_string(platform) in stored_states:
        break
    stored_states.append(plat_to_string(platform))

first_occurrence = stored_states.index(plat_to_string(platform))
cycles = len(stored_states) - first_occurrence
platform = string_to_plat(stored_states[(1000000000 - first_occurrence) % cycles + first_occurrence])

print('Day 14 Part 2:',sum([sum([1 for x in p if x == 'O']) * i for i,p in enumerate(platform[::-1])]))
