impl Solution {
    pub fn largest_palindrome(n: i32) -> i32 {
        if n == 1 {
            return 9; 
        }
        let upper: i64 = 10i64.pow(n as u32) - 1; 
        let mut left: i64 = upper; 
        while left > upper / 10 {
            let mut pal: i64 = left; 
            let mut x: i64 = left; 
            while x > 0 {
                pal = pal * 10 + x % 10; 
                x /= 10; 
            }
            x = upper; 
            while x as f64 >= (pal as f64).sqrt() {
                if pal % x == 0 {
                    return (pal % 1337) as i32; 
                }
                x -= 1; 
            }
            left -= 1; 
        }
        panic!(); 
    }
}

struct Solution {}

fn main() {
    // assert_eq!(Solution::largest_palindrome(1), 9); 
    assert_eq!(Solution::largest_palindrome(2), 987); 
    // assert_eq!(Solution::largest_palindrome(7), 877); 
}