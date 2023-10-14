use std::collections::HashMap;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut count = HashMap::new(); 
        for num in nums.iter() {
            *count.entry(num).or_insert(0) += 1; 
        }
        for (num, count) in count {
            if count == 1 {
                return *num; 
            }
        }
        0
    }
}