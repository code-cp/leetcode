impl Solution {
    pub fn count_pairs(nums: Vec<i32>, low: i32, high: i32) -> i32 {
        let mut count = 0; 
        let n = nums.len(); 
        for i in 0..n {
            for j in i+1..n {
                let r = nums[i] ^ nums[j]; 
                if r <= high && r >= low {
                    count += 1; 
                }
            }
        }
        count 
    }
}