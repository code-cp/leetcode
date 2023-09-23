use std::cmp::{min, max};

// struct Solution;

impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let m = (n + 1) / 2 + 1;
        let mut dp = vec![vec![f64::INFINITY; 2]; m];
        let mut ans = f64::INFINITY;

        for i in 1..=n {
            let mut tmp = dp.clone(); 
            if i == 1 {
                tmp[1][1] = nums[i - 1] as f64;
            } else if i == 2 {
                tmp[1][0] = dp[1][1];
                tmp[1][1] = nums[i - 1] as f64;
            } else {
                for j in 1..m {
                    tmp[j][0] = dp[j][0].min(dp[j][1]);
                    if j == 1 {
                        tmp[j][1] = nums[i - 1] as f64;
                    } else if dp[j - 1][0].is_finite() {
                        tmp[j][1] = dp[j - 1][0].max(nums[i - 1] as f64);
                    }
                }
            }
            dp = tmp.clone(); 
            ans = ans.min(dp[k as usize][0]).min(dp[k as usize][1]);
        }

        ans as i32
    }
}