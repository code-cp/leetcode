struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len(); 
        let mut dp = vec![vec![0; 4]; n]; 

        // holds stock  
        dp[0][0] = -prices[0];
        // no stock, sell today
        // NOTE, do not forget this state  
        // if without this state, then 
        // can buy and sell on the same day 
        // which is forbidden 
        dp[0][1] = 0; 
        // no stock no cool down 
        dp[0][2] = 0; 
        // cooldown 
        dp[0][3] = 0; 

        for i in 1..n {
            // hold stock 
            dp[i][0] = (dp[i-1][2] - prices[i]).max((dp[i-1][3] - prices[i]).max(dp[i-1][0]));
            // no stock sell today 
            dp[i][1] = dp[i-1][0] + prices[i];
            // no stock no cool down 
            dp[i][2] = std::cmp::max(dp[i-1][2], dp[i-1][3]);    
            // sell -> cool down  
            dp[i][3] = dp[i-1][1]; 
        }

        dp[n-1][1].max(dp[n-1][2].max(dp[n-1][3]))
    }
}

fn main() {
    let prices = vec![1,2,4]; 
    let result = Solution::max_profit(prices); 
}
