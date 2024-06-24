class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        end = len(num)
        self.ans = set()

        def backtrack(start, value, last_num, expr):
            if start == end:
                if value == target:
                    self.ans.add(expr)
                return

            for i in range(start, end):
                curr_num = int(num[start : i + 1])
                # curr_num = int(curr_num_st)

                if start == 0:
                    backtrack(i + 1, curr_num, curr_num, str(curr_num))
                else:
                    backtrack(
                        i + 1,
                        value + curr_num,
                        curr_num,
                        expr + "+" + str(curr_num),
                    )
                    backtrack(
                        i + 1,
                        value - curr_num,
                        -curr_num,
                        expr + "-" + str(curr_num),
                    )
                    backtrack(
                        i + 1,
                        value - last_num + last_num * curr_num,
                        last_num * curr_num,
                        expr + "*" + str(curr_num),
                    )

                if curr_num == 0:
                    break

        backtrack(0, 0, 0, "")
        return self.ans

        # def Util(self, ind, mem, exp):
        #     if ind == l - 1:
        #         exp += num[ind]
        #         if eval(exp) == target:
        #             return [exp]
        #     if ind >= l:
        #         return []
        #     ret1 = self.Util(ind + 1, mem, exp + str(num[ind]) + '+')
        #     ret2 = self.Util(ind + 1, mem, exp + str(num[ind]) + '-')
        #     ret3 = self.Util(ind + 1, mem, exp + str(num[ind]) + '*')
        #     if (exp and exp[-1].isdigit() is True and num[ind] == '0') or num[ind] != '0':
        #         ret4 = self.Util(ind + 1, mem, exp + str(num[ind]))
        #         ret = ret1 + ret2 + ret3 + ret4
        #     else:
        #         ret = ret1 + ret2 + ret3
        #     return ret

    # def addOperators(self, num: str, target: int) -> List[str]:
    #     return self.Util(0, len(num), '')
