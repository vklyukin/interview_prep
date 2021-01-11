import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            last_1 = -heapq.heappop(stones)
            last_2 = -heapq.heappop(stones)

            if last_1 > last_2:
                heapq.heappush(stones, last_2 - last_1)

        if not stones:
            return 0
        else:
            return -stones[0]
