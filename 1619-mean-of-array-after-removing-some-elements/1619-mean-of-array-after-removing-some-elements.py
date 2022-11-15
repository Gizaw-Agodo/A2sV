class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        
        newarr = arr[n*5//100:n*95//100]
        return sum(newarr)/len(newarr)

            