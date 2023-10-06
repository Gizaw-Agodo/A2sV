class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for index, (num, denom) in enumerate(equations):
            graph[num].append((denom, values[index]))
            graph[denom].append((num , 1/values[index]))
        
        def dfs(node, dest, visited):
            if node not in graph or dest not in graph:
                return -1
            
            if node == dest:
                return 1

            for child, val in graph[node]:
                if child not in visited:
                    visited.add(child)
                    curr_value = val*dfs(child, dest, visited)
                    
                    if curr_value > 0 :
                        return curr_value

            return -1

        answer = []
        for start, destin in queries:
            answer.append(dfs(start, destin, set()))

        return answer
            






