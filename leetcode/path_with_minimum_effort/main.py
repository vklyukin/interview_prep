import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_rows = len(heights)
        num_columns = len(heights[0])

        visited = set()
        distances = [
            [float("inf") for _ in range(num_columns)] for _ in range(num_rows)
        ]

        current_cell = (0, 0)
        distances[0][0] = 0

        heap = []
        heapq.heappush(heap, (distances[0][0], current_cell))

        while heap:
            current_distance, current_cell = heapq.heappop(heap)

            if current_cell in visited:
                continue

            visited.add(current_cell)

            if (
                current_cell[0] > 0
                and (current_cell[0] - 1, current_cell[1]) not in visited
            ):
                distances[current_cell[0] - 1][current_cell[1]] = min(
                    distances[current_cell[0] - 1][current_cell[1]],
                    max(
                        current_distance,
                        abs(
                            heights[current_cell[0] - 1][current_cell[1]]
                            - heights[current_cell[0]][current_cell[1]]
                        ),
                    ),
                )
                heapq.heappush(
                    heap,
                    (
                        distances[current_cell[0] - 1][current_cell[1]],
                        (current_cell[0] - 1, current_cell[1]),
                    ),
                )

            if (
                current_cell[1] > 0
                and (current_cell[0], current_cell[1] - 1) not in visited
            ):
                distances[current_cell[0]][current_cell[1] - 1] = min(
                    distances[current_cell[0]][current_cell[1] - 1],
                    max(
                        current_distance,
                        abs(
                            heights[current_cell[0]][current_cell[1] - 1]
                            - heights[current_cell[0]][current_cell[1]]
                        ),
                    ),
                )
                heapq.heappush(
                    heap,
                    (
                        distances[current_cell[0]][current_cell[1] - 1],
                        (current_cell[0], current_cell[1] - 1),
                    ),
                )

            if (
                current_cell[0] + 1 < num_rows
                and (current_cell[0] + 1, current_cell[1]) not in visited
            ):
                distances[current_cell[0] + 1][current_cell[1]] = min(
                    distances[current_cell[0] + 1][current_cell[1]],
                    max(
                        current_distance,
                        abs(
                            heights[current_cell[0] + 1][current_cell[1]]
                            - heights[current_cell[0]][current_cell[1]]
                        ),
                    ),
                )
                heapq.heappush(
                    heap,
                    (
                        distances[current_cell[0] + 1][current_cell[1]],
                        (current_cell[0] + 1, current_cell[1]),
                    ),
                )

            if (
                current_cell[1] + 1 < num_columns
                and (current_cell[0], current_cell[1] + 1) not in visited
            ):
                distances[current_cell[0]][current_cell[1] + 1] = min(
                    distances[current_cell[0]][current_cell[1] + 1],
                    max(
                        current_distance,
                        abs(
                            heights[current_cell[0]][current_cell[1] + 1]
                            - heights[current_cell[0]][current_cell[1]]
                        ),
                    ),
                )
                heapq.heappush(
                    heap,
                    (
                        distances[current_cell[0]][current_cell[1] + 1],
                        (current_cell[0], current_cell[1] + 1),
                    ),
                )

        return distances[-1][-1]