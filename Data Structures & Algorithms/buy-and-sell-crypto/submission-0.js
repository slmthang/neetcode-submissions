class Solution {
    /**
     * @param {number} prices
     * @return {number}
     */
    maxProfit(prices) {

        let profit = 0;
        let min = prices[0];
        let max = min;

        for (let i = 1; i < prices.length; i++) {

            if (prices[i] < min ) {
                    
                min = prices[i];
                max = min;
            } else if (prices[i] > max) {

                max = prices[i];

                if (max - min > profit) {
                    profit = max - min;
                }
            }
            
        }

        return profit;
    }
}
