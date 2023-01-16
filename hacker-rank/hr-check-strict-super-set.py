set_a = set(str(input()).split(" "))

n = len(set_a)
count = int(input())
flag =True
for i in range(count):
    curr_input = set(str(input()).split(" "))    
    if not set_a.issuperset(curr_input):
        flag = False
        print(False)
        break
if flag:
    print(True)
