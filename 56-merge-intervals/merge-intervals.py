class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        ## Case 1:
        # <-------->
        #    <--------> => min(start), max(end)
        #    <-->
        #             <---->  if curr_start > prev_end => ignore
        intervals.sort(key = lambda a: a[0])
        merged_interval = []
        for interval in intervals:
            if not merged_interval:
                merged_interval.append(interval)
                continue
            
            curr_start, curr_end = interval[0], interval[1]
            prev_start, prev_end = merged_interval[-1][0], merged_interval[-1][1] 
            if curr_start > prev_end:
                merged_interval.append(interval)
                continue
            else:
                merged_interval[-1][1] = max(curr_end, prev_end)
        
        return merged_interval
            
            

            
        