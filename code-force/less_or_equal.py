n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
if arr[k-1] >= 1 and arr[k-1] <= 1*10**9:
    if k < len(arr)+1 and arr[k] != arr[k-1]:
        print(arr[k-1])
else:
    print(-1)
