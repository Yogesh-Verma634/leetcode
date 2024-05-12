class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.sum = 0
        self.arr = []
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.sum += val
        self.arr.append(val)

        if (self.count <= self.size):
            return (self.sum / self.count)
        
        oldest_val = self.arr.pop(0)
        # print(oldest_val)
        self.sum -= (oldest_val)
        return (self.sum / self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)