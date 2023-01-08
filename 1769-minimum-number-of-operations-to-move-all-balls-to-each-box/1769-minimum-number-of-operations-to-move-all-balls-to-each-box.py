class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        dic = {}
        for i,num in enumerate(boxes):
            dic[num] = i
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    count += abs(j-i)
            answer.append(count)
        return answer
