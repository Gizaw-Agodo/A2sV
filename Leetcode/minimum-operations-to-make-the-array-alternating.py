class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oddCount = defaultdict(int)
        evenCount = defaultdict(int)
        firstEvenMax = (-1, 0)
        secondEvenMax = (-1, 0)
        firstOddMax = (-1, 0)
        secondOddMax = (-1, 0)

        for index, num in enumerate(nums):
            if index%2 == 0:
                evenCount[num] += 1
                if evenCount[num] > firstEvenMax[1]:
                    firstEvenMax = (num, evenCount[num])
                elif evenCount[num] > secondEvenMax[1]:
                    secondEvenMax = (num , evenCount[num])
            else:
                oddCount[num] += 1
                if oddCount[num] > firstOddMax[1]:
                    firstOddMax = (num, oddCount[num])
                elif oddCount[num] > secondOddMax[1]:
                    secondOddMax = (num, oddCount[num])
        
        if firstEvenMax[0] != firstOddMax[0]:
            return len(nums) - (firstOddMax[1] + firstEvenMax[1])
        else:
            case1 = firstOddMax[1] + secondEvenMax[1]
            case2 = firstEvenMax[1] + secondOddMax[1]
            return len(nums) - max(case1, case2)
        
        
