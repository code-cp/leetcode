use std::cmp::{min, max};

// struct Solution;

impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let m = (n + 1) / 2 + 1;
        let mut dp = vec![vec![vec![f64::INFINITY; 2]; m]; n + 1];
        let mut ans = f64::INFINITY;

        for i in 1..=n {
            if i == 1 {
                dp[i][1][1] = nums[i - 1] as f64;
            } else if i == 2 {
                dp[i][1][0] = dp[i - 1][1][1];
                dp[i][1][1] = nums[i - 1] as f64;
            } else {
                for j in 1..m {
                    dp[i][j][0] = dp[i - 1][j][0].min(dp[i - 1][j][1]);
                    if j == 1 {
                        dp[i][j][1] = nums[i - 1] as f64;
                    } else if dp[i - 1][j - 1][0].is_finite() {
                        dp[i][j][1] = dp[i - 1][j - 1][0].max(nums[i - 1] as f64);
                    }
                }
            }
        }

        for i in 1..=n {
            ans = ans.min(dp[i][k as usize][0]).min(dp[i][k as usize][1]);
        }

        ans as i32
    }
}