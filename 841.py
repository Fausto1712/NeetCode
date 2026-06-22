from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room: int) -> None:
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)

        
if __name__ == "__main__":
    solution = Solution()

    rooms = [[1],[2],[],[3]]
    print("Result:", solution.canVisitAllRooms(rooms))