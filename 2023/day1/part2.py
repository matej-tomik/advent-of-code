def find_digit(ln: str, directio: str):
    if directio == 'from_front':
        directio = 1
    else:
        directio = -1
    my_dist = {}
    for character in ln[::directio]:
        if character.isdigit():
            my_dist.update({character: ln[::directio].index(character)})
    for num in number:
        if ln.find(num) != -1:
            my_dist.update({num: ln[::directio].index(num[::directio])})
    return my_dist

def get_num(my_dist: dict):
    tmp = min(my_dist, key=my_dist.get)
    if tmp in number:
        return number.index(tmp) + 1
    else:
        return tmp


number = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
with open('input.txt', 'r') as f:
    total = 0
    for line in list(map(str.rstrip, f.readlines())):
        total += int(str(get_num(find_digit(line, 'from_front'))) + str(get_num(find_digit(line, 'from_back'))))
    print(total)
