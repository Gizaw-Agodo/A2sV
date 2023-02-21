n, m = list(map(int, input().split()))

first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

start_first = 0
start_second = 0

ans = []
while start_first < n and start_second < m:
    if first_arr[start_first] <= second_arr[start_second]:
        ans.append(first_arr[start_first])
        start_first += 1
    else:
        ans.append(second_arr[start_second])
        start_second += 1
if start_first < n:
    ans.extend(first_arr[start_first:])
elif start_second < m:
    ans.extend(second_arr[start_second:])
print(*ans)
