class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        # firstList.sort()
        # secondList.sort()

        while i < len(firstList) and j < len(secondList):
            # 1. Check overlap between current pointers to firstList and secondList
            # 2. Whichever ends first, move the pointer
            # 3. If there's overlap, take max(start_times) and min(end_times)

            ## Check if firstList is starting first
            # => Does secondList start lie in between firstList => overlap

            f_start, f_end = firstList[i][0], firstList[i][1]
            s_start, s_end = secondList[j][0],secondList[j][1]

            if s_start <= f_start <= s_end or f_start <= s_start <= f_end:
                overlap_start = max(f_start, s_start)            
                overlap_end = min(firstList[i][1], secondList[j][1])
                res.append([overlap_start, overlap_end])

            if firstList[i][1] == secondList[j][1]:
                i += 1
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

            

        return res




            