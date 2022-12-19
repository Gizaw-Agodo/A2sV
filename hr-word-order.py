
from collections import defaultdict
length = int(input())
mylist = []

for i in range(length):
    mylist.append(input())
    
mydict = defaultdict(int)
distinict = 0
for value in mylist:
    if value not in mydict:
        distinict +=1
    mydict[value] += 1
    
print(distinict)
for value in mydict:
    print(mydict[value], end= " ")
