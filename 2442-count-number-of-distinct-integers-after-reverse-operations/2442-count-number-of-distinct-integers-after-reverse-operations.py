class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = []
        arr += nums
        for elem in nums:
            revers = reversed(list(str(elem)))
            elem = int("".join(list(revers)))
            arr.append(elem)
       
        return len(set(arr))