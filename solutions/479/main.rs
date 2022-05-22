use std::collections::BinaryHeap;
impl Solution {
    pub fn is_pal(n: i64) -> bool {
        let mut num = n; 
        let mut rev = 0; 
        let mut p = (n as f64).log10() as u32; 
        while num > 0 {
            rev += 10i64.pow(p) * (num % 10); 
            num /= 10; 
            p = if p >= 1 {p-1} else {0}; 
        } 
        return rev == n;
    }
    pub fn largest_palindrome(n: i32) -> i32 {
        let n = n as u32; 
        let mut pq = BinaryHeap::new(); 
        for i in (10i64.pow(n-1)-1..10i64.pow(n)-1).rev() {
            pq.push((i * (10i64.pow(n)-1), i, 10i64.pow(n)-1));
        }
        loop {
            let (res, i, j) = pq.pop().unwrap(); 
            if Solution::is_pal(res) {
                return (res % 1337) as i32; 
            } 
            pq.push((i * (j-1), i, j-1)); 
        }
    }
}

struct Solution {}

fn main() {
    // assert_eq!(Solution::largest_palindrome(1), 9); 
    assert_eq!(Solution::largest_palindrome(7), 877); 
}