# input() version 174 char, payload 79 char

# from collections import Counter
# l,r=zip(*sorted([*map(int,l.split())]for l in input()))
# print(sum(abs(a-b)for a,b in zip(*map(sorted,(l,r)))),sum(Counter(r)[x]*x for x in l))

# runnable version 176 char
from collections import Counter
l,r=zip(*sorted([*map(int,l.split())]for l in open('i')))
print(sum(abs(a-b)for a,b in zip(*map(sorted,(l,r)))),sum(Counter(r)[x]*x for x in l))