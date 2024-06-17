class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        heap = [[k, v] for k, v in count_map.items()]
        heapq.heapify(heap)

        return [k for k, v in heapq.nlargest(k, heap, key=lambda e: e[1])]


            
