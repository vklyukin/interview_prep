class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square_size = 0
        max_square = [[0] * len(matrix[0]) for _ in matrix]

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == "1":
                    left_square = max_square[i][j + 1] if j + 1 < len(matrix[i]) else 0
                    bottom_square = max_square[i + 1][j] if i + 1 < len(matrix) else 0
                    left_bottom_square = (
                        max_square[i + 1][j + 1]
                        if (i + 1 < len(matrix)) and (j + 1 < len(matrix[i]))
                        else 0
                    )

                    max_square[i][j] = 1 + min(
                        left_square, bottom_square, left_bottom_square
                    )
                    max_square_size = max(max_square_size, max_square[i][j])

        return max_square_size * max_square_size
