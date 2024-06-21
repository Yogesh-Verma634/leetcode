class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len(customers) <= minutes:
            return sum(customers)

        curr_sum = max_unsatisfied_cust = sum([customers[idx] * grumpy[idx] for idx in range(0, minutes)])
        i, j = 0, minutes

        for j in range(minutes, len(customers)):
            curr_sum = curr_sum + customers[j] * grumpy[j] - customers[i] * grumpy[i]
            if curr_sum > max_unsatisfied_cust:
                max_unsatisfied_cust = curr_sum
            i += 1

        max_customer = max_unsatisfied_cust
        for idx, customer in enumerate(customers):
            if grumpy[idx] == 0:
                max_customer += customer

        return max_customer
        