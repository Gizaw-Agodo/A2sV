class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #monotonic increasing stack
        stack = [0]
        arr = [0] + arr
        contigSum =  [0]*len(arr)
    
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            index = stack[-1] 
            contigSum[i] = contigSum [index] + arr[i]*(i-index)
            stack.append(i)
        
        return sum(contigSum) % (10**9+7)
            