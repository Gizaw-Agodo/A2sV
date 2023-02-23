length = int(input())
nums = list(map(int,input().split()))

is_even = False
is_odd = False

for num in nums:
  if num%2 : 
    is_odd = True
  else:
    is_even = True

if is_odd and is_even:
  nums.sort()
  print(*nums)
else:
  print(*nums)
