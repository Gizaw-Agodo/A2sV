from collections import Counter
testCases = int(input())


for i in range(testCases):
    n, cost = input().split()
    orbit = input().split()
    count = Counter(orbit)
    expence = 0
    for key, values in count.items():
        if values < int(cost):
            expence += values
        else:
            expence += int(cost)
    print(expence)
