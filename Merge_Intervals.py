class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            pre_end = res[-1][1]
            
            #overlapping interval
            if start <= pre_end:
                res[-1][1] = max(end, pre_end) # merge intervals
            
            #non-overlapping 
            else:
                res.append([start, end]) # keep both intervals
        
        return res
