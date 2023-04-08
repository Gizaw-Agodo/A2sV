class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(set)
        for source,destin in roads:
            dic[source].add(destin)
            dic[destin].add(source)
        
        maximum = float("-inf")
        for i in range(n):
            for j in range(i+1,n):
                if j in dic[i]:
                    curr_net = len(dic[i]) + len(dic[j]) - 1
                else:
                    curr_net = len(dic[i]) + len(dic[j])
                maximum = max(curr_net, maximum)
        return maximum
                