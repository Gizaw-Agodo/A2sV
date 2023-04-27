class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])
        
        def bfs(rooms):
            
            while queue :
                curr_room = queue.popleft()
                for value in rooms[curr_room]:
                    if value not in visited:
                        visited.add(value)
                        queue.append(value)
        bfs(rooms)
        return len(visited) == len(rooms)
        
        