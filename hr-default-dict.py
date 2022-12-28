# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m= input().split()
dic = defaultdict(list)
for i in range(int(n)):
    curr_input = input()
    dic[curr_input].append(i+1) 

for j in range(int(m)):
    curr = input()
    if len(dic[curr]) == 0:
        print(-1)
    else:
        for k in range(len(dic[curr])):
            print(dic[curr][k] ,end = " ")
        print()
        
