class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        parents = list(range(n))
        parents[firstPerson] = 0
        rank = [1]*n
        
        def find(x):
            if parents[x] != x:
                 parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            if p1 != p2:
                if p1 == 0 or p2 == 0:
                    parents[p1] = parents[p2] = 0
               
                else:
                    if rank[p1] >= rank[p2]:
                        parents[p2] = p1
                        rank[p1] += rank[p2]
                    else:
                        parents[p1] = p2
                        rank[p2] += rank[p1]
        
        meetings.sort(key=lambda m:m[2])
        N = len(meetings)
        i = 0
        while i < N:
            sameTimeMeetings = [meetings[i]]
            while i < N-1 and meetings[i+1][2] == meetings[i][2]:
                i = i+1
                sameTimeMeetings.append(meetings[i])
                continue
            
            for x,y,time in sameTimeMeetings:
                union(x, y)

            for x,y,time in sameTimeMeetings:
                rootX = find(x)

                if rootX != 0:
                    parents[x] = x
                    parents[y] = y
                            
            i+=1

        return [i for i in range(n) if find(i) == 0]
