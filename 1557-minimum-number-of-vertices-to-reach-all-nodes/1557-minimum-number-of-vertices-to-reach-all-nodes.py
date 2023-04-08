class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0]*n
        for source,destin in edges:
            inDegree[destin] += 1
        answer = []
        for i in range(n):
            if inDegree[i] == 0:
                answer.append(i)
        return answer