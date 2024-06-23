class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left = 0
        max_window = 0
        min_heap = []
        max_heap = []
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        for idx, num in enumerate(nums):
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

            min_, max_ = min_heap[0], -max_heap[0]

            if (max_ - min_) > limit:
                # if min_heap[0] == nums[left]:
                min_heap.remove(nums[left])
                
                # if -max_heap[0] == nums[left]:
                max_heap.remove(-nums[left])
                left += 1
                heapq.heapify(min_heap)
                heapq.heapify(max_heap)
            
            max_window = max(max_window, idx-left+1)

        return max_window