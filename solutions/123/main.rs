struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut dp = vec![vec![0; 5]; n]; 

        // no action 
        dp[0][0] = 0;
        // 1st buy 
        dp[0][1] = -prices[0]; 
        // 1st sell 
        dp[0][2] = 0; 
        // 2nd buy 
        dp[0][3] = -prices[0]; 
        // 2nd sell 
        dp[0][4] = 0; 

        for i in 1..n {
            dp[i][0] = dp[i-1][0]; 
            // either already buy at i-1, or buy at i 
            dp[i][1] = std::cmp::max(dp[i-1][1], dp[i-1][0]-prices[i]);
            dp[i][2] = std::cmp::max(dp[i-1][2], dp[i-1][1]+prices[i]);
            dp[i][3] = std::cmp::max(dp[i-1][3], dp[i-1][2]-prices[i]); 
            dp[i][4] = std::cmp::max(dp[i-1][4], dp[i-1][3]+prices[i]); 
        }

        std::cmp::max(dp[n-1][1], dp[n-1][4])
    }
}