n = int(input())
alchemy = list(map(int, input().split()))
edwardTime = 0
alphonseTime = 0
edwardcount = 0
alphonsecount = 0

left = 0
right = n-1

while left <= right :
    if left == 0 and right == n-1:
        edwardTime = alchemy[left]
        alphonseTime = alchemy[right]
        left += 1
        right -= 1

    if edwardTime <= alphonseTime :
        edwardTime += alchemy[left]
        left += 1
        edwardcount += 1
        
    elif alphonseTime < edwardTime:
        alphonseTime += alchemy[right]
        right -= 1
        alphonsecount += 1

print(edwardcount, alphonsecount)
