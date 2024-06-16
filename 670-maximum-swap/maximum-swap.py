class Solution:
    def maximumSwap(self, num: int) -> int:

        num = [int(x) for x in str(num)]

        max_seen, max_seen_at = -1, len(num)

        for idx, n in enumerate(num[::-1]):
            idx = len(num) - idx - 1

            num[idx] = (n, max_seen, max_seen_at)
            if n > max_seen:
                max_seen = n
                max_seen_at = idx
        
        for i in range(len(num)):
            n, max_seen, max_seen_at = num[i]

            if max_seen > n:
                num[i], num[max_seen_at]= num[max_seen_at], num[i]
                break

        res = 0
        n = 0
        for curr_num, _, _ in num:
            n = n*10 + curr_num
        return n
            
            
        