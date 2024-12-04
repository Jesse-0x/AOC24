def safe(level):
    diff = [level[i+1] - level[i] for i in range(len(level)-1)]
    if any(abs(d) < 1 or abs(d) > 3 for d in diff):
        return 0
    return all(d > 0 for d in diff) or all(d < 0 for d in diff)

data = []
for line in open('i'):
    data.append(list(map(int,line.split())))

# part 1
print(sum(map(safe, data)))

# part 2
# print(sum(any(safe(l[:i]+l[i+1:])for i in range(len(l)))for l in r))
c = 0

for level in data:
    for i in range(len(level)):
        if safe(level[:i] + level[i+1:]):
            c += 1
            break

print(c)