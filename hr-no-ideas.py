m,n = input().split(" ")
feed = input().split(" ")
a_element = set(input().split(' '))
b_element = set(input().split( ' '))
hapiness = 0
for element in feed : 
    if element in a_element : 
        hapiness +=1
    elif element in b_element:
        hapiness -=1
print(hapiness)
