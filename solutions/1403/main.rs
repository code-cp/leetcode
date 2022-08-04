impl Solution {
    pub fn min_subsequence(nums: Vec<i32>) -> Vec<i32> {
        use std::collections::BinaryHeap; 
        let target = nums.iter().sum::<i32>() / 2; 

        let mut heap = nums.into_iter().collect::<BinaryHeap<i32>>(); 

        let mut ans = Vec::new();
        let mut acc = 0; 
        while acc <= target {
            let t = heap.pop().unwrap(); 
            ans.push(t);
            acc += t
        }
        ans 
    }
}