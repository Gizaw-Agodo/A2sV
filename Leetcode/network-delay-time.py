class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')]*(n + 1)
        distances[k] = 0

        graph = defaultdict(list)
        for start, end , time in times:
            graph[start].append((end, time))
       
        stack = [(0, k)]
        visited = set()

        while stack:
           
            distance, node = heappop(stack)

            visited.add(node)
            for endNode, d in graph[node]:
                currDistance = distance + d
                if currDistance < distances[endNode] and endNode not in visited:
                    distances[endNode] = currDistance
                    heappush(stack, (currDistance, endNode))

        maximum = max(distances[1:])
        return maximum if maximum != float('inf') else -1
        
