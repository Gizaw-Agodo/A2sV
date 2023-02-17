n = int(input())
data = list(map(int,input().split()))

data.sort()
if  len(set(data)) == 1:
  print(-1)
else:
  print(*data)
