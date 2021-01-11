class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        elif len(grid) == 1:
            return sum(grid[0])

        min_path_upper = grid[0]

        for i in range(1, len(min_path_upper)):
            min_path_upper[i] += min_path_upper[i - 1]

        for i in range(1, len(grid)):
            min_path_cur = grid[i].copy()
            min_path_cur[0] += min_path_upper[0]

            for j in range(1, len(min_path_cur)):
                min_path_cur[j] += min(min_path_upper[j], min_path_cur[j - 1])
            min_path_upper = min_path_cur

        return min_path_cur[-1]
