from collections import defaultdict
k = input()
roomList = input().split(" ")

dic = defaultdict(int)
for element in roomList:
    dic[element] +=1
for element in dic:
    if dic[element] == 1:
        print(element)
