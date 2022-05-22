use std::collections::HashSet; 

struct Solution {}

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut my_set = HashSet::new(); 
        for i in 0..nums.len() {
            if my_set.contains(&nums[i]) {
                return true; 
            }
            my_set.insert(nums[i]);
            if i >= k as usize {
                my_set.remove(&nums[i-k as usize]);
            }
        }
        return false; 
    }
}

fn main() {
    assert!(Solution::contains_nearby_duplicate(vec![1,2,3,1], 3))
}
