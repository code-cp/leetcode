fn main() {
    assert_eq!(Solution::dominant_index(vec![3, 6, 1, 0]), 1);
}

struct Solution {}

impl Solution {
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        let mut max_val = std::i32::MIN;
        let mut max_id: i32 = 0;
        let mut second_max = std::i32::MIN;
        for i in 0..nums.len() {
            if nums[i] > max_val {
                second_max = max_val;
                max_val = nums[i];
                max_id = i as i32;
            }
            else if nums[i] > second_max {
                second_max = nums[i];
            }
        }
        if max_val >= 2*second_max {
            max_id
        }
        else {
            -1i32
        }
    }
}
