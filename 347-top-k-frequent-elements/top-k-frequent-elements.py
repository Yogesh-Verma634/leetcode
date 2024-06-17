class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        heap = [[k, v] for k, v in count_map.items()]
        heapq.heapify(heap)

        # while len(heap) == k:
        #     heapq.heappop(heap)
        return [k for k, v in heapq.nlargest(k, heap, key=lambda e: e[1])]
        # return []

        # if len(nums) == k:
        #     return nums
        # reverse_count = defaultdict(list)

        # for key, val in count_map.items():
        #     reverse_count[val].append(key)
        
        # keys = list(sorted(reverse_count.keys(), reverse=True))

        # res = []

        # for key in keys:
        #     for val in reverse_count[key]:
        #         if len(res) == k:
        #             return res
        #         res.append(val)
        # return res


            
