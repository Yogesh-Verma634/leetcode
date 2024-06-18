class Solution:

    def __init__(self, nums: List[int]):
        self.nums_map = defaultdict(list)

        for idx, num in enumerate(nums):
            self.nums_map[num].append(idx)

    # def random_pick(self, arr_idx):
    #     return 

    def pick(self, target: int) -> int:
        indices = self.nums_map[target]

        ## Implement random pick
        idx = random.randint(0, len(indices)-1)
        return indices[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)