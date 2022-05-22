struct Solution {}

impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        let mut result: i32 = 0; 
        let mut num: i32 = num; 
        while num > 0 {
            if num & 1 == 1 {
                num -= 1; 
            }
            else {
                num >>= 1; 
            }
            result += 1; 
        }
        return result; 
    }
}

fn main() {
    assert_eq!(Solution::number_of_steps(14), 6); 
}

