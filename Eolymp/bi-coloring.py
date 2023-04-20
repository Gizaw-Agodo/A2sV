from collections import defaultdict

def dfs(node , curr_color , color_array ,adj_list):
    color_array[node] = curr_color

    for neibhour in adj_list[node]:
        if color_array[neibhour] == curr_color:
            return False
        elif not dfs(neibhour, 1-curr_color,color_array,adj_list):
            return False
    return True


while True:
    n = int(input())
    e = int(input())
    if n == 0:
        break
    adj_list = defaultdict(set)
    color = [-1]*n

    for i in range(e):
        node1,node2 = list(map(int,input().split()))
        adj_list[node1 - 1].add(node2 - 1)
        adj_list[node2 - 1].add(node1 - 1 )

    flag = True
    for key in adj_list:
        if color[key] == -1:
            if not dfs(key,0,color,adj_list):
                flag = False
                break
    
    if flag :
        print('BICOLOURABLE.')
    else:
        print('NOT BICOLOURABLE.')
