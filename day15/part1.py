f = open('data.txt').read().strip().split(',')
total = 0
for string in f:
    tmp = 0
    for character in string:
        tmp = ((tmp + ord(character)) * 17) % 256
    total += tmp
print(total)