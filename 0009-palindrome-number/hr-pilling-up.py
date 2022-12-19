t = int(input())

for i in range(t):
    maximum = float("inf")
    flag = True
    n = int(input())
    cubes = input().split(' ')
    left = 0 
    right = n - 1

    while left < right :
        if int(cubes[left]) >= int(cubes[right]) and int(cubes[left])<=maximum:
            maximum = int(cubes[left])
            left +=1
        elif int(cubes[right]) >= int(cubes[left]) and int(cubes[right])<=maximum:
            maximum = int(cubes[right])
            right-=1
        else:
            print("No")
            flag = False
            break
    if flag:
        print("Yes")
