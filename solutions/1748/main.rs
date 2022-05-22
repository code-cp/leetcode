use std::collections::HashMap; 

struct Solution {}

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new(); 
        nums.iter().for_each(|c| *counter.entry(*c).or_insert(0) += 1); 
        counter.iter().filter(|(_, v)| **v == 1).map(|(k, _)| *k).sum::<i32>()
    }
}

fn main() {
    assert_eq!(Solution::sum_of_unique(vec![1,2,3,2]), 4);
}