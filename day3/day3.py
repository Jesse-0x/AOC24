import re

data = open('input.txt').read()
p1 = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
total = 0

# part 1
total = sum(int(x) * int(y) for x, y in p1.findall(data))
print(total)


# Part 2
total, lock = 0, True

def mul(a, b):
    return a * b

for c in re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', data):
    if c == 'do()':
        lock = True
    elif c == "don't()":
        lock = False
    elif lock:
        total += int(eval(c))

print(total)