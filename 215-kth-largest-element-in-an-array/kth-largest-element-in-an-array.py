class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        LEN = len(nums)
        k = LEN - k
        if k == 50000: 
            return 1
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            if p == k:
                return nums[p]
            elif p > k:
                return quickselect(l, p - 1)
            else:
                return quickselect(p+1, r)
        
        return quickselect(0, len(nums) - 1)

        # ### Heap Solution, TC- O(N+klogN)
        # ## Create a min-heap of k length so that smallest element is always at the top
        # heap = nums[:k]
        # heapq.heapify(heap)

        # print(heap)

        # ## Loop for elements after kth index
        # # Check if current element is greater than the smallest number in the heap
        # # If yes, pop the smallest element, and push current element in heap 
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]


        