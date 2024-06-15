class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ## Quick select
        def partition(low, high):
            pivot_idx = random.randint(low, high)
            pivot = distances[pivot_idx][0]
            
            distances[high], distances[pivot_idx] = distances[pivot_idx], distances[high]

            for curr in range(low, high):
                curr_val = distances[curr][0]
                if curr_val < pivot:
                    distances[low], distances[curr] = distances[curr], distances[low]
                    low += 1
            
            distances[low], distances[high] = distances[high], distances[low]
            return low

        def quickselect(low, high):
            while low < high:
                pivot = partition(low, high)

                if pivot == k:
                    return
                elif pivot < k:
                    low = pivot + 1
                    # quickselect(pivot + 1, high)
                else:
                    high = pivot - 1
                    # quickselect(low, pivot - 1)
            
        distances = [(x**2+y**2, (x, y)) for x, y in points]

        quickselect(0, len(distances)-1)

        return [point for _, point in distances[:k]]

        ### Using Heap
        # res = []
        # heapq.heapify(res)

        # for idx, (x, y) in enumerate(points):
        #     d = -(x*x + y*y)
        #     heapq.heappush(res, (d, [x, y]))

        #     if len(res) > k:
        #         heapq.heappop(res)

        # return [(x, y) for d, [x, y] in res]

