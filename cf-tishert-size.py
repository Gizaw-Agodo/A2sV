n = int(input())
for i in range(n):
    size1,size2 = input().split()
    if size2 == size1:
        print("=")
    elif size1[-1] > size2[-1]:
        print("<")
    elif size1[-1] < size2[-1]:
        print(">")
    elif size1[-1] == "L" and len(size1) > len(size2):
        print(">")
    elif size1[-1] == "S" and len(size1) < len(size2):
        print(">")
    else:
        print("<")
