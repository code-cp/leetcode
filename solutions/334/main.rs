fn main() {
    assert!(Solution::increasing_triplet(vec![1,2,3,4,5]));
}

struct Solution {}

impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let mut first_val: i32 = i32::MAX;
        let mut second_val: i32 = i32::MAX;
        for i in 0..nums.len() {
            if nums[i] < first_val {
                first_val = nums[i];
            }
            else if nums[i] > first_val && nums[i] < second_val {
                second_val = nums[i];
            }
            else if nums[i] > second_val {
                return true;
            }
        }
        false
    }
}

