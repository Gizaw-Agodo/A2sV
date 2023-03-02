import sys


def superDigit(n, k):
    def findSuper(n):
        if len(n) == 1:
            return int(n)
        curr_sum = sum(map(int,list(n)))
        return int(findSuper(str(curr_sum)))
    
    curr_super = str(findSuper(n))
    return findSuper(curr_super*k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
