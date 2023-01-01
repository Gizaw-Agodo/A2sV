from collections import defaultdict
test = int(input())

for i in range(test):
    n = int(input())
    array = input().split()
    string = input()

    dic = defaultdict(list)
    for i in range(n):
        dic[array[i]].append(i)
    flag = False
    for key,values in dic.items():
        if len(values) >1: 
            init = string[values[0]]
            for val in values:
                if string[val] != init:
                    print("NO")
                    flag  = True
                    break
            if flag:
              break
    if not flag:        
        print("YES")
