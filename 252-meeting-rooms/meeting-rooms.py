class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        #### Cases
        # <------->
        #    <------> => Any such overlaps is False, else True
        times_occupied = set()

        for curr_start, curr_end in intervals:
            for curr_time in range(curr_start, curr_end):
                if curr_time in times_occupied:
                    return False
                times_occupied.add(curr_time)
        return True

        #### Sorting Solution => TC - Nlog(N), SC - O(1)
        # if not intervals:
        #     return True
        # intervals.sort()
        
        # for idx in range(1, len(intervals)):
        #     prev_start, prev_end = intervals[idx-1][0], intervals[idx-1][1]
        #     curr_start, curr_end = intervals[idx][0], intervals[idx][1]

        #     if curr_start < prev_end:
        #         return False
        
        return True

