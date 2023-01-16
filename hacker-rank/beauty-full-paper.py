T = int(input())
for _ in range(T):
    a1, b1 = list(map(int, input().split()))
    a2, b2 = list(map(int, input().split()))

    max_side1 = max(a1, b1)
    max_side2 = max(a2, b2)
    min_side1 = min(a1, b1)
    min_side2 = min(a2, b2)
    if max_side1 == max_side2 and max_side1 == min_side1 + min_side2:
        print("Yes")
    else:
        print("No")
