t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))

    minimum = min(a, b)
    answer = min(minimum, (a + b)//4)
    print(answer)
