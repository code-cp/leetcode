impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut dp = 0; 
        let mut pre = nums[0]; 
        for i in 1..nums.len() {
            let cur = (pre+1).max(nums[i]); 
            dp += cur - nums[i]; 
            pre = cur; 
        }
        dp 
    }
}