class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        answer = [""]*len(names)
        for i in range(len(heights)):
            heights[i] = [heights[i],i]
        heights.sort(key = lambda x :-x[0])
        
        for i in range(len(names)):
            height,index = heights[i]
            
            answer[i] = names[index]
        return answer