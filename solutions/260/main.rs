struct Solution; 

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let xor_result = nums.iter().fold(0, |acc, &x| acc ^ x); 
        let low_bit = xor_result & (-xor_result); 
        let mut ans = vec![0, 0]; 
        for &x in nums.iter() {
            if (x & low_bit) == 0 {
                ans[0] ^= x; 
            } else {
                ans[1] ^= x; 
            }
        }
        ans
    }
}