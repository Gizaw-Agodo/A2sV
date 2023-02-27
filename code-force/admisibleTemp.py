n, k, q = map(int, input().split())

count = [0] * 200001
for i in range(len(count)):
    left, right = map(int, input().split())
    count[left] += 1
    count[right+1] -= 1

for i in range(1, len(count)):
  count[i] += count[i-1]

for i in range(len(count)):
    count[i] = 1 if count[i] >= k else 0
    
for i in range(1, 200001):
    count[i] += count[i-1]

for i in range(q):
    a, b = map(int, input().split())
    print(count[b] - count[a-1])
