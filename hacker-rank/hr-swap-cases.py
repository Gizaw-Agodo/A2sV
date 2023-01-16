def swap_case(s):
    mylist = [i for i in s]
    for i in range(len(s)):
        if mylist[i].isalpha():
            if mylist[i].isupper():
                mylist[i] = mylist[i].lower()
            else:
                mylist[i] = mylist[i].upper()
        
    return "".join(mylist)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
