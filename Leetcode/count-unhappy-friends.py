class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = []
        for i in range(len(preferences)):
            temp = [n]*n
            value = preferences[i]
            for j in range(len(value)):
                temp[value[j]] = j
            pref.append(temp)
        
        ans = set()
        for x, y in pairs:
            for u,v in pairs:    
                if pref[x][u] < pref[x][y] and pref[u][x] < pref[u][v]:
                    ans = ans.union({x,u})
                if pref[y][v] < pref[y][x] and pref[v][y] < pref[v][u]:
                    ans = ans.union({y,v})
                if pref[x][v] < pref[x][y] and pref[v][x] < pref[v][u]:
                    ans = ans.union({x,v})
                if pref[y][u] < pref[y][x] and pref[u][y] < pref[u][v]:
                    ans = ans.union({y,u})
                      
        return len(ans)
        
