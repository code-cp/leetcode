struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        // The transaction fee is only charged once for each stock purchase and sale
        // means only charged once for buy+sell, not buy charge once and sell charge once

        let n = prices.len(); 
        let mut dp = vec![vec![0; 2]; n]; 

        // no stock 
        dp[0][0] = 0;
        // hold stock 
        dp[0][1] = -prices[0]; 

        for i in 1..n {
            dp[i][0] = std::cmp::max(dp[i-1][0], dp[i-1][1] + prices[i] - fee);
            dp[i][1] = std::cmp::max(dp[i-1][0] - prices[i], dp[i-1][1]); 
        }

        dp[n-1][0]
    }
}