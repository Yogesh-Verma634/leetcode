class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)

        for idx, (x, y) in enumerate(points):
            d = -(x*x + y*y)
            heapq.heappush(res, (d, [x, y]))

            if len(res) > k:
                heapq.heappop(res)

        return [(x, y) for d, [x, y] in res]

