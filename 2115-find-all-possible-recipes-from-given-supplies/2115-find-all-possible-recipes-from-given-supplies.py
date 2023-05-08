class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph  = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        prepared = set()
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
            
        for supply in supplies :
            indegree[supply] = 0
            queue.append(supply)
        
        for i in range(len(recipes)):
            indegree[recipes[i]] = len(ingredients[i])
        
        while queue:
            
            recipe = queue.popleft()
            prepared.add(recipe)
            for ing in graph[recipe]:
                indegree[ing] -= 1
                if indegree[ing] == 0:
                    queue.append(ing)
        answer = []
        
        for recipe in recipes :
            if recipe in prepared:
                answer.append(recipe)
                
        return answer 
            
        
        
        
        
        