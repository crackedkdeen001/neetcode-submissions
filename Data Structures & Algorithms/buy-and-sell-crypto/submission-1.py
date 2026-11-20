class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force

        max_profit = 0
        for i in range(len(prices)):
            selling_price = prices[i]
            
            # we set the cost prices to equal to the smallest value so far
            # since we're trying to maximize profit
            if i == 0:
                cost_price = prices[i]
            else:
                cost_price = min(cost_price, selling_price)
            
            profit = selling_price - cost_price
            max_profit = max(max_profit, profit)

        return max_profit

