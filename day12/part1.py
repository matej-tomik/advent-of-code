from itertools import product
import re

f = open('data.txt').read().strip()
springs = [x.split() for x in f.strip().split('\n')]
springs = [[x[0], [int(y) for y in x[1].split(',')]] for x in springs]



def count_permutations(symbols):
    results = set()
    for symbol, counts in symbols:
        possibilities = []
        for s in symbol:
            if s == '?':
                possibilities.append(['#', '.'])
            else:
                possibilities.append([s])

        for combo in product(*possibilities):
            candidate = ''.join(combo)
            matches = re.findall(r'#+', candidate)
            match_lengths = [len(x) for x in matches]
            if match_lengths == counts:
                results.add(str(candidate))

    return len(results)


total = [count_permutations([s]) for s in springs]

print(sum(total))
