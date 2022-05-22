struct Solution {}

impl Solution {
    pub fn num_to_digits(mut num: i32) -> Vec<i32> {
        let mut digits = Vec::new(); 
        while num > 0 {
            digits.push(num % 10);
            num /= 10; 
        }
        digits
    }
    pub fn add_digits(num: i32) -> i32 {
        let mut result = num; 
        while result >= 10 {
            let digits = Solution::num_to_digits(result);
            result = digits.iter().fold(0, |total, i| total + i); 
        }
        result 
    }
}

fn main() {
    assert_eq!(Solution::add_digits(38), 2); 
    assert_eq!(Solution::add_digits(10), 1);
}