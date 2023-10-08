class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        count = 0
        def dfs(root, parent):
            nonlocal count
            
            currSum = values[root]
            
            for child in graph[root]:
                if child == parent :
                    continue
                currSum += dfs(child, root)
            
            if currSum % k == 0:
                count += 1
                currSum = 0

            return currSum

        dfs(0,-1)
        return count

                
