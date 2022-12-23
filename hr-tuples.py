if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    set_to_tuple = tuple(integer_list)
    print(hash(set_to_tuple))
