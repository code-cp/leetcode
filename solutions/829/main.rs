// # sum = x + x+1 + ... + x+w-1 = N
// # (x + x+w-1) * w / 2 = N 
// # (2x-1 + w) * w = 2N 
// # 2x-1 + w > w 

impl Solution {
    pub fn bsearch(n: i32, w: i64) -> bool {
        let n = n as i64; 
        let mut l = 0; 
        let mut r = n; 
        while l <= r {
            let m = (r - l) / 2 + l; 
            // note the overflow 
            let sum: i64 = (m + m+w-1) * w / 2; 
            if sum > n {
                r = m - 1; 
            } else if sum < n {
                l = m + 1; 
            } else {
                return true;  
            }
        }
        return false; 
    }
    pub fn consecutive_numbers_sum(n: i32) -> i32 {
        let mut count = 0; 
        let max_w = ((2*n) as f64).sqrt() as i64; 
        for w in 1..max_w+1 {
            if Solution::bsearch(n, w) {
                count += 1; 
            }
        }
        return count; 
    }
}

struct Solution {}

fn main() {
    assert_eq!(2, Solution::consecutive_numbers_sum(5)); 
}