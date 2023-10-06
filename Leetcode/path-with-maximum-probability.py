class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for index, (start, end) in enumerate(edges):
            graph[start].append((end, succProb[index]))
            graph[end].append((start, succProb[index]))

        probablity = [float('-inf')]*n
        probablity[start_node] = 1

        heap = [(-1, start_node)]
        visited = set()

        while heap:
            prob, node = heappop(heap)

            for child, child_prob in graph[node]:
                curr_prob = abs(prob)*child_prob
                
                if curr_prob > probablity[child] and child not in visited:
                    probablity[child] = curr_prob
                    heappush(heap, (-1*curr_prob, child))

        return probablity[end_node] if probablity[end_node] != float('-inf') else 0


