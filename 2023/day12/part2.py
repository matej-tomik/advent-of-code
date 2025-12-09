from functools import cache


f = open('data.txt').read().strip()
springs = [x.split() for x in f.strip().split('\n')]
springs = [(x[0], tuple(map(int, x[1].split(',')))) for x in springs]
springs = [('?'.join([x[0]] * 5) + '.', x[1] * 5) for x in springs]


@cache
def count_permutations(symbols, counts, group_loc=0):
    if not symbols:
        return not counts and not group_loc
    results = 0
    if symbols[0] == '?':
        possibilities = ['.', '#']
    else:
        possibilities = symbols[0]

    for p in possibilities:
        if p == '#':
            results += count_permutations(symbols[1:], counts, group_loc + 1)
        else:
            if group_loc > 0:
                if counts and counts[0] == group_loc:
                    results += count_permutations(symbols[1:], counts[1:])
            else:
                results = results + count_permutations(symbols[1:], counts)
    return results


total = [count_permutations(s[0], s[1]) for s in springs]
print(sum(total))
