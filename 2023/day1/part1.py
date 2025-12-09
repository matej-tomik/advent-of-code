def find_digit(line: str) -> str:
    for character in line:
        if character.isdigit():
            return character


with open('input.txt', 'r') as f:
    lines = list(map(str.rstrip, f.readlines()))
    print(sum([int(find_digit(line) + find_digit(line[::-1])) for line in lines]))
