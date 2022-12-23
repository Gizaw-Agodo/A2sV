if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        command = str(input()).split(" ")

        if command[0] == "print":
            print(my_list)
        elif command[0] == "insert":
            my_list.insert(int(command[1]),int(command[2]))
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "reverse":
            my_list.reverse()
        elif command[0] == "pop":
            my_list.pop()
        
