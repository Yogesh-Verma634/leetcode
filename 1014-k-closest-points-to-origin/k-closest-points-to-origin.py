class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)

        def distance(x, y):
            return math.sqrt(int(x*x + y*y))

        for idx, (x, y) in enumerate(points):
            d = distance(x, y)
            heapq.heappush(res, (-d, [x, y]))

            if len(res) > k:
                heapq.heappop(res)
                
        final_res = []
        for val, point in res:
            final_res.append(point)

        return final_res

