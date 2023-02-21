n = int(input())
temp_list = list(map(int, input().split()))

list_negative = []
list_positive = []
list_zero = []

for elem in temp_list:
    if elem < 0 :
        list_negative.append(elem)
    elif elem ==0 : 
        list_zero.append(elem)
    else:
        list_positive.append(elem)

if len(list_negative) %2 == 0:
    list_negative.append(list_negative.pop())
if len(list_positive) == 0:
    list_positive.append(list_negative.pop())
    list_negative.append(list_negative.pop())


print(len(list_negative), end=" ")

for i in range(len(list_negative)):
    if i != len(list_negative)-1:
        print(list_negative[i], end=" ")
    else:
        print(list_negative[i])

print(len(list_positive), end=" ")

for i in range(len(list_positive)):
    if i != len(list_positive)-1:
        print(list_positive[i], end=" ")
    else:
        print(list_positive[i])

print(len(list_zero), end=" ")

for i in range(len(list_zero)):
    if i != len(list_zero)-1:
        print(list_zero[i], end=" ")
    else:
        print(list_zero[i])
