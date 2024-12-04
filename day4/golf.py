# input() version 205 char, payload 162 char

# g=[l.strip().upper()for l in input()]
# f=lambda s:s in('MAS','SAM')
# print(sum(f(g[i-1][j-1]+g[i][j]+g[i+1][j+1])&f(g[i-1][j+1]+g[i][j]+g[i+1][j-1]) for i in range(1,len(g)-1) for j in range(1,len(g[0])-1)))


# runnable version 211 char
g=[l.strip().upper()for l in open('i')]
f=lambda s:s in('MAS','SAM')
print(sum(f(g[i-1][j-1]+g[i][j]+g[i+1][j+1])&f(g[i-1][j+1]+g[i][j]+g[i+1][j-1])for i in range(1,len(g)-1)for j in range(1,len(g[0])-1)))
