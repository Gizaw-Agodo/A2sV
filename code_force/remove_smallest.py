t = int(input())

for i in range(t):
    n = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    flag = False
    for i in range(n-1):
        if num_list[i+1] > num_list[i] + 1:
            print("NO")
            flag = True
            break
    if not flag:
        print("YES")
