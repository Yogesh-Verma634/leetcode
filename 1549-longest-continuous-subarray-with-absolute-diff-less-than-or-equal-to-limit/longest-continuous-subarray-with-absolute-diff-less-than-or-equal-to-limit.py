class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left = 0
        max_window = 1
        min_heap = []
        max_heap = []
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        for right, num in enumerate(nums):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            while min_heap[0][1] < left:
                heapq.heappop(min_heap)
            while max_heap[0][1] < left:
                heapq.heappop(max_heap)

            if -max_heap[0][0] - min_heap[0][0] <= limit:
                # if it's valid, we can update the answer
                max_window = max(max_window, right - left + 1)
            else:
                # else we just move the left end of the window
                left += 1
        return max_window