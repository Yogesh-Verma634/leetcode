class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        min_f, max_f = 1, (max(position) - min(position))//(m-1)
        
        def force_possible(force, max_balls):
            last_pos = position[0]

            for n in range(1, len(position)):
                curr = position[n]
                if (curr-last_pos) >= force:
                    max_balls -= 1                   
                    last_pos = curr
                
                if not max_balls:
                    return True

            return False

        res_f = -1

        while min_f <= max_f:
            mid = (min_f + max_f) // 2

            if force_possible(mid, m-1):
                res_f = mid
                min_f = mid + 1
            else:
                max_f = mid - 1
        
        return res_f

        

            

        