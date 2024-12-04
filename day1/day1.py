from collections import Counter

l = []
r = []

for line in open('input.txt', 'r'):
    total = line.strip().split()
    l.append(int(total[0]))
    r.append(int(total[1]))

l.sort()
r.sort()

# part 1
print(sum(abs(a - b) for a, b in zip(l, r)))


# part 2
f=Counter(r)
print(sum(num * f[num] for num in l))