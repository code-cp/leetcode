fn main() {
    assert_eq!(Solution::gray_code(2), [0,1,3,2]);
}

struct Solution {} 

impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        let mut dp = vec![0; 1 << n];
        let mut count;
        let mut to_add;
        for i in 1..(n+1) {
            count = 1 << i;
            to_add = 1 << (i-1);
            for j in count/2..count {
                dp[j] = dp[count-1-j] + to_add;
            }
        }
        dp
    }
}


