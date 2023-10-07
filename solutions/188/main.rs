struct Solution; 

impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        let k = k as usize; 
        let mut dp = vec![vec![0; 2*k+1]; prices.len()]; 
        
        // init 
        for i in 1..=2*k {
            // dp[0][i] is buy when i%2 == 1 
            dp[0][i] = -prices[0]; 
        }

        for i in 1..prices.len() {
            // no action 
            dp[i][0] = dp[i-1][0];
            for j in 1..=2*k {
                if j % 2 == 1 {
                    // buy 
                    dp[i][j] = std::cmp::max(dp[i-1][j], dp[i-1][j-1]-prices[i]); 
                } else {
                    // sell
                    dp[i][j] = std::cmp::max(dp[i-1][j], dp[i-1][j-1]+prices[i]);
                }
            } 
        }

        let mut ans = 0;
        for i in 1..prices.len() {
            for j in 1..=2*k {
                // only consider sell operations 
                if j % 2 == 0 {
                    ans = std::cmp::max(ans, dp[i][j]);
                }
            }
        }

        ans 
    }
}