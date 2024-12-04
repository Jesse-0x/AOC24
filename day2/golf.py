# input() version 211 char, payload 166 char

# s=lambda l:all(0<abs(b-a)<4for a,b in zip(l,l[1:]))and l in(sorted(l),sorted(l)[::-1])
# r=[list(map(int,l.split()))for l in input()]
# print(sum(map(s,r)),sum(any(s(l[:i]+l[i+1:])for i in range(len(l)))for l in r))

# runnable version 211 char
s=lambda l:all(0<abs(b-a)<4for a,b in zip(l,l[1:]))and l in(sorted(l),sorted(l)[::-1]);r=[list(map(int,l.split()))for l in open('i')];print(sum(map(s,r)),sum(any(s(l[:i]+l[i+1:])for i in range(len(l)))for l in r))