struct Solution {}

// ref https://leetcode-cn.com/problems/optimal-division/solution/rust-553-zui-you-chu-fa-by-fffzlfk-k7y4/
impl Solution {
    pub fn optimal_division(nums: Vec<i32>) -> String {
        match nums.len() {
            1 => nums[0].to_string(), 
            2 => format!("{}/{}", nums[0], nums[1]), 
            _ => format!("{}/({})",
                    nums[0], 
                    nums[1..]
                        .iter()
                        .map(|num| num.to_string())
                        .collect::<Vec<String>>()
                        .join("/")
                    ), 
        }
    }
}

fn main() {
    assert_eq!(Solution::optimal_division(vec![1000,100,10,2]), "1000/(100/10/2)"); 
}