from collections import defaultdict
n = int(input())
k = int(input())

dic = defaultdict(list)
for i in range(k):
    operation = list(map(int,input().split()))
    if operation[0] == 1:
        dic[operation[1]].append(operation[2])
        dic[operation[2]].append(operation[1])
    else:
        print(*dic[operation[1]])
