def merge(left_half , right_half,count):
    
    if left_half[-1]<= right_half[0]:
        return[left_half + right_half, count]
    elif left_half[0] < right_half[-1]:
        return [[],-1]
    else:
        return [right_half + left_half, count + 1]     

def mergeSort(left, right, arr):
    if left == right:
        return [[arr[left]],0]
    mid = left + (right - left) // 2
    left_half, count1 = mergeSort(left, mid, arr)
    right_half, count2 = mergeSort(mid + 1, right, arr)
    if count1 == -1 or count2 == -1:
        return [[],-1]
    return merge(left_half, right_half,count2 + count1)

t = int(input())
for i in range(t):
    m = int(input())
    array =list( map(int, input().split()))
    sorted,count = mergeSort(0, len(array)-1, array)
    print(count)
