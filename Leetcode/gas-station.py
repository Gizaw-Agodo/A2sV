class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        totalGas = 0
        currGas = 0

        for i in range(n):
            totalGas +=  gas[i] - cost[i]
            currGas +=  gas[i] - cost[i]
            
            if currGas < 0:
                currGas = 0
                start =  i + 1

        return -1 if totalGas < 0   else start
