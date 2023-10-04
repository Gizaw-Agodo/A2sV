class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        dist = [[float('inf')]*numCourses for _ in range(numCourses)]
        
        for start, end in prerequisites:
            dist[start][end] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        
        return [dist[i][j] != float('inf') for i, j in queries]
        
