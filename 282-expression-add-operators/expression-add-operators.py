class Solution:
    def Util(self, num, target, ind, l, mem, exp):
        if ind == l - 1:
            exp += num[ind]
            if eval(exp) == target:
                return [exp]
        if ind >= l:
            return []
        ret1 = self.Util(num, target, ind + 1, l, mem, exp + str(num[ind]) + '+')
        ret2 = self.Util(num, target, ind + 1, l, mem, exp + str(num[ind]) + '-')
        ret3 = self.Util(num, target, ind + 1, l, mem, exp + str(num[ind]) + '*')
        if (exp and exp[-1].isdigit() is True and num[ind] == '0') or num[ind] != '0':
            ret4 = self.Util(num, target, ind + 1, l, mem, exp + str(num[ind]))
            ret = ret1 + ret2 + ret3 + ret4
        else:
            ret = ret1 + ret2 + ret3
        return ret
        
    def addOperators(self, num: str, target: int) -> List[str]:
        return self.Util(num, target, 0, len(num), dict(), '')
        # if len(num) <= 0:
        #     return int(num) == target
        # self.ans = []
        # end = len(num)

        # def dfs(start, last_num, value, expression):
        #     if start == end:
        #         if value == target:
        #             self.ans.append(expression)
        #         return

        #     last_num = int(last_num)
        #     curr_num = int(num[start])
        #     ## for add operation
        #     sum_exp = f"{expression}+{num[start]}"
        #     ## for subtract operation
        #     sub_exp = f"{expression}-{num[start]}"
        #     ## for multiply operation
        #     multi_exp = f"{expression}*{num[start]}"
        #     ## for combination operation
        #     combine_exp = f"{expression}" + num[start]
        #     combined_val = value - last_num + int(str(last_num) + num[start])


        #     if start == 0:
        #         dfs(start+1, int(num[0]), int(num[0]), f"{num[0]}")
        #     else:
        #         dfs(start+1, curr_num, value + curr_num, sum_exp)
        #         dfs(start+1, -curr_num, value - curr_num, sub_exp)

        #         curr_value = last_num * curr_num + (value - last_num)
        #         dfs(start+1, last_num * curr_num, curr_value, multi_exp)
                
        #         if last_num == 0:
        #             return
        #         else:
        #             dfs(start+1, int(str(last_num) + num[start]) , int(combined_val), combine_exp) 

        # dfs(0, 0, 0, "")
        # print(len(self.ans))
        # return self.ans