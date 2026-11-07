import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, -(a-b))

        if stones:
            return -stones[0]

        return 0