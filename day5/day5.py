from collections import defaultdict, deque
import networkx as nx

def topo(pages, rules):
    G = nx.DiGraph()
    G.add_nodes_from(pages)
    G.add_edges_from((x, y) for x, y in rules if x in pages and y in pages)
    return list(nx.topological_sort(G))


data = open('input.txt', 'r').read()

rule, update = data.strip().split('\n\n')

rules = []
for line in rule.split('\n'):
    rules.append((*map(int, line.split('|')),))

updates = []
for line in update.split('\n'):
    updates += [list(map(int, line.split(',')))]

rt = 0
rt2 = 0

for i in updates:
    pos = {page: idx for idx, page in enumerate(i)}

    flag = True
    for x, y in rules:
        if x in pos and y in pos:
            if pos[x] >= pos[y]:
                flag = False
                break
    if flag:
        rt += i[len(i) // 2]
    else:
        upd = topo(i, rules)
        rt2 += upd[len(upd) // 2]

print(rt)
print(rt2)