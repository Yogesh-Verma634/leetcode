class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n-1):                                # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i+1]: break
        else: return num                                    # if nothing find, return num
        max_idx, max_val = i+1, s[i+1]                      # keep going right, find the maximum value index
        for j in range(i+1, n):
            if max_val <= s[j]: max_idx, max_val = j, s[j]
        left_idx = i                                        # going left from 0 to i, find most left value that is less than max_val
        for j in range(i + 1):    
            if s[j] < max_val: 
                left_idx = j
                break
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]   # swap maximum after i and most left less than max
        return int(''.join(s))                              # re-create the integer

        # num = [int(x) for x in str(num)]

        # max_seen, max_seen_at = -1, len(num)

        # for idx, n in enumerate(num[::-1]):
        #     idx = len(num) - idx - 1

        #     num[idx] = (n, max_seen, max_seen_at)
        #     if n > max_seen:
        #         max_seen = n
        #         max_seen_at = idx
        
        # for i in range(len(num)):
        #     n, max_seen, max_seen_at = num[i]

        #     if max_seen > n:
        #         num[i], num[max_seen_at]= num[max_seen_at], num[i]
        #         break

        # res = 0
        # n = 0
        # for curr_num, _, _ in num:
        #     n = n*10 + curr_num
        # return n
            
            
        