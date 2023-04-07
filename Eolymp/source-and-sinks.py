from collections import defaultdict
n = int(input())
dictionary = defaultdict(list)

for i in range(n):
    array = list(map(int,input().split()))
    for j in range(len(array)):
        dictionary[i].append((j,array[j]))

sourcesCandidate = set()
sinksCandidate = set()

for i in range(n):
    for j in range(n):
        if dictionary[i][j]==1:
            sourcesCandidate.add(i)
            sinksCandidate.add(j)

sources = []
sinks = []

for i in range(len(sourcesCandidate)):
    if sourcesCandidate[i] not in sinksCandidate:
        sources.append(sourcesCandidate[i])

for i in range(len(sinksCandidate)):
    if sinksCandidate[i] not in sourcesCandidate:
        sinks.append(sinksCandidate[i])

set_union = sourcesCandidate.union(sinksCandidate)

for i in range(n):
    if i not in set_union:
        sources.append(i)
        sinks.append(1)

sources.sort()
sinks.sort()

print(len(sources), *sources)

print(len(sinks), *sinks)
