struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // 0 means do not pick current house
        let mut dp = vec![vec![0; 2]; n]; 
        for i in 0..n {
            if i == 0 {
                dp[i][1] = nums[0];
                continue;  
            } else if i == 1 {
                dp[i][0] = dp[i-1][1]; 
                dp[i][1] = nums[1]; 
                continue; 
            } else {
                dp[i][0] = dp[i-1][1].max(dp[i-1][0]);
                dp[i][1] = dp[i-1][0] + nums[i]; 
            }
        }
        dp[n-1][0].max(dp[n-1][1])
    }
}