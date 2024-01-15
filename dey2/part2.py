import re
import copy
import math


f = open("data.txt", "r")
balls = {
    'red': 0,
    'green': 0,
    'blue': 0
}
total_count = 0
for line in f:
    line_list = re.split('; |, |: ', line.rstrip('\n '))
    max_no_balls = copy.deepcopy(balls)
    for ball in line_list[1:]:
        value, key = ball.split(' ')
        if int(max_no_balls[key]) < int(value):
            max_no_balls[key] = int(value)
    total_count += math.prod(max_no_balls.values())
print(total_count)
