Struct Solution; 

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len(); 
        if n == 1 {
            return nums[0];
        } 

        let mut nums = nums; 
        let mut dp1 = vec![vec![0;2];n-1];
        let mut dp2 = vec![vec![0;2];n-1]; 

        for (i, &num) in nums.iter().take(n-1).enumerate() {
            if i == 0 {
                dp1[i][1] = num;  
            } else if i == 1 {
                dp1[i][0] = dp1[i-1][1]; 
                dp1[i][1] = num; 
            } else {
                dp1[i][0] = dp1[i-1][0].max(dp1[i-1][1]); 
                dp1[i][1] = dp1[i-1][0] + num; 
            }
        }

        nums.reverse(); 
        for (i, &num) in nums.iter().take(n-1).enumerate() {
            if i == 0 {
                dp2[i][1] = num;  
            } else if i == 1 {
                dp2[i][0] = dp2[i-1][1]; 
                dp2[i][1] = num; 
            } else {
                dp2[i][0] = dp2[i-1][0].max(dp2[i-1][1]); 
                dp2[i][1] = dp2[i-1][0] + num; 
            }    
        }

        return dp1[n-2][0].max(dp1[n-2][1].max(dp2[n-2][0].max(dp2[n-2][1])));
    }
}

