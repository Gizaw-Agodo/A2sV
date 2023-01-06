class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pt1 = 0
        pt2  = 0
        posetives = []
        negetives = []
        answer = []
        for num in nums:
            if num > 0 :
                posetives.append(num)
            else:
                negetives.append(num)
        
        for i in range(len(negetives)):
            answer.append(posetives[i])
            answer.append(negetives[i])
        return answer
            