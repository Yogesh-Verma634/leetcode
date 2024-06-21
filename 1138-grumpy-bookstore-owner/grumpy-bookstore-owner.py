class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len(customers) <= minutes:
            return sum(customers)

        curr_sum = max_unsatisfied_cust = sum([customers[idx] * grumpy[idx] for idx in range(0, minutes)])
        unsatis_idx = minutes-1
        i, j = 0, minutes

        while j < len(customers):
            if grumpy[i] == 1:
                curr_sum -= customers[i]
            if grumpy[j] == 1:
                curr_sum = curr_sum + customers[j]
                
            if curr_sum > max_unsatisfied_cust:
                max_unsatisfied_cust = curr_sum
                unsatis_idx = j

            i += 1
            j += 1
        max_customer = 0
        low, high = unsatis_idx - minutes + 1 , unsatis_idx
        for idx, customer in enumerate(customers):
            if grumpy[idx] == 0 or (low <= idx <= high):
                max_customer += customer

        return max_customer
        