'''import random
lines = open("newfile.txt").read().splitlines()
print(random.choice(lines))
'''
import random
def random_line(fname):
    lines = open(fname).readlines()
    return random.choice(lines)
print(random_line('html.txt'))