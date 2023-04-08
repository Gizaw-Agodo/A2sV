n = int(input())
ans = []
for i in range(n):
    array = list(map(int, input().split()))
    for j in range(len(array)):
        if array[j] == 1 and [j,i] not in ans:
            ans.append([i,j])
            
print(len(ans))
