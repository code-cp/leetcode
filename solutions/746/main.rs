impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let n = cost.len(); 
        let mut dp = vec![0;n+1]; 
        for i in 2..=n {
            dp[i] = (dp[i-2] + cost[i-2]).min(dp[i-1] + cost[i-1]); 
        }
        dp[n]
    }
}