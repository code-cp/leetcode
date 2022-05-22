use std::collections::HashMap; 

struct Solution {}

impl Solution {
    pub fn count_k_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut umap = HashMap::new(); 
        let mut result = 0; 
        for n in nums {
            result += *umap.entry(n).or_insert(0); 
            *umap.entry(n-k).or_insert(0) += 1; 
            *umap.entry(n+k).or_insert(0) += 1; 
        }
        result 
    }
}

fn main() {
    assert_eq!(Solution::count_k_difference(vec![1,2,2,1], 1), 4); 
}