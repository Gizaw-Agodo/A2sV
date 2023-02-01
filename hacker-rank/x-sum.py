from collections import defaultdict

t = int(input())
for i in range(t):
  n,m = map(int,input().split())
  grid = []
  for i in range(n):
    curr_input = list(map(int,input().split()))
    grid.append(curr_input)
  
  left_diagonal_sum = defaultdict(int)
  for i in range (len(grid)):
    for j in range(len(grid[0])):
      left_diagonal_sum[abs(i-j)] += grid[i][j]
  
  right_diagonal_sum = defaultdict(int)
  for i in range (len(grid)):
    for j in range(len(grid[0])):
      right_diagonal_sum[i+j] += grid[i][j]
  
  max_sum = float("-inf")
  for i in range (len(grid)):
    for j in range(len(grid[0])):
      
      curr_sum = left_diagonal_sum[abs(i-j)] + right_diagonal_sum[i+j] - grid[i][j]
      max_sum = max(curr_sum , max_sum)
  print(max_sum)
