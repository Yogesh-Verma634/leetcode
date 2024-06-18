class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        worker.sort()
        max_profit = 0
        difficultyProfit = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        difficultyProfit.sort()
        sorted(difficultyProfit, key=lambda x: x[0])
        for i in range(len(difficulty)):
            max_profit = max(max_profit, difficultyProfit[i][1])
            difficultyProfit[i] = [difficultyProfit[i][0], max_profit]

        
        max_profit = 0

        diff_ptr = 0
        curr_profit = 0

        for w in worker:
            while diff_ptr < len(difficultyProfit):
                difficulty = difficultyProfit[diff_ptr][0]
                profit = difficultyProfit[diff_ptr][1]
                
                if w >= difficulty:
                    curr_profit = profit
                    diff_ptr += 1
                else:
                    break
            
            max_profit += curr_profit
        
        return max_profit

        