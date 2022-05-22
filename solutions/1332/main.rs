struct Solution {}

impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        let is_palindrome = |s: String| {
            let half_len: usize = (s.len() / 2) as usize;
            s.chars().take(half_len).eq(s.chars().rev().take(half_len))
        };
        if is_palindrome(s) {
            return 1;
        }
        else {
            return 2;
        }
    }
}

fn main() {
    assert_eq!(Solution::remove_palindrome_sub("baabb".to_string()), 2);
}
