fn main() {
    assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), [0, 1]);
}

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in (i+1)..nums.len() {
                if nums[j] == target - nums[i] {
                    return vec![i as i32, j as i32]
                }
            }
        }
        vec![]
    }
}

#[cfg(test)]
mod test {
    use crate::*;
    #[test]
    fn simple_test() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), [0, 1]);
    }
}
