class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        # dfs + dp explained and committed 
        # first find the total cost assuming no cost are halved 
        # then use dp to choose which node to half and get maximum reduction

        #  create tree Node
        tree = defaultdict(list)
        for start, end in edges:
            tree[start].append(end)
            tree[end].append(start)
 
        # calculating total cost and nodes on path count using dfs
        count = defaultdict(int)
        totalCost = 0

        def dfs (parent, node, end):
            nonlocal count
            nonlocal totalCost

            if node == end: 
                return True

            for child in tree[node]:
                if child != parent:
                    if dfs(node, child, end):
                        totalCost += price[child]
                        count[child] += 1
                        return True
            return False


        for start, end in trips:
            count[start] += 1
            totalCost += price[start]
            dfs(None, start, end)


        # calculating the maximum value to be reduced using dp
        @cache
        def dp(isRedusable, parent, node):
            response = 0
            
            if isRedusable:
                response += ((price[node])//2)*count[node]

            reduction = 0
            for child in tree[node]:
                if parent != child :
                    if isRedusable: 
                        reduction  +=  dp(False, node, child)
                    else:
                        reduced = dp(True,node, child)
                        notReduced = dp( False, node, child)
                        maximum = max(reduced, notReduced)
                        reduction += maximum

            return reduction + response
        

        totalReduction = 0
        for i in range(n):
            takeIt = dp(True, None, i)
            leaveIt = dp(False, None, i)
            totalReduction  = max(totalReduction, takeIt, leaveIt)
        
        return totalCost - totalReduction

        




        
        
