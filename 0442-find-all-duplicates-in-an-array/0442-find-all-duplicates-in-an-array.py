class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        answer = []
        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        for key in dic:
            if dic[key] == 2:
                answer.append(key)
        return answer
            
        
        