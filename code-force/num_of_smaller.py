n,m = map(int,input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

answer  = 0
p1 = 0
answer = []
for i in range(len(list2)):
    while p1 < len(list1) and list1[p1] < list2[i]:
        p1 += 1
    answer.append(p1)
print(*answer)
