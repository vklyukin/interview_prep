class Solution:
    def dfs(self, i: int, j: int, visited: List[List[bool]], grid: List[List[str]]):
        to_visit = [(i, j)]

        while to_visit:
            x, y = to_visit.pop()
            visited[x][y] = True
            if x > 0 and grid[x - 1][y] == "1" and not visited[x - 1][y]:
                to_visit.append((x - 1, y))
            if y > 0 and grid[x][y - 1] == "1" and not visited[x][y - 1]:
                to_visit.append((x, y - 1))
            if x + 1 < len(grid) and grid[x + 1][y] == "1" and not visited[x + 1][y]:
                to_visit.append((x + 1, y))
            if y + 1 < len(grid[x]) and grid[x][y + 1] == "1" and not visited[x][y + 1]:
                to_visit.append((x, y + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in grid]
        num_islands = 0

        for i in range(len(grid)):
            for j, val in enumerate(grid[i]):
                if not visited[i][j]:
                    if val == "1":
                        self.dfs(i, j, visited, grid)
                        num_islands += 1
                    else:
                        visited[i][j] = True

        return num_islands