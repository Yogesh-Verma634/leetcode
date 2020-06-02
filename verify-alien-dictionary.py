class Solution:
    def isAlienSorted(self, words, order):
        order_index =  {c: i for i, c in enumerate(order)}
        
        for idx in range(1, len(words)):
            prev = words[idx-1]
            curr = words[idx]
            
            def checkAlien(prev, curr):
                for idx in range(min(len(prev), len(curr))):
                    if prev[idx] != curr[idx]:
                        if order_index[prev[idx]] > order_index[curr[idx]]:
                            return False
                        return True
                
                if len(prev) < len(curr):
                    return True
        
            if not checkAlien(prev, curr):
                return False
        return True

solution = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(solution.isAlienSorted(words, order))