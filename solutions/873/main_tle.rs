// TLE
impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        let n = arr.len(); 
        let mut dp = vec![vec![0; n]; n]; 
        let mut result = 0; 
        if arr[2] == arr[0] + arr[1] {
            dp[2][1] = 3; 
            result = 3; 
        }
        for i in 3..n {
            for j in 0..i {
                for k in 0..j {
                    if arr[k] + arr[j] == arr[i] {
                        if dp[j][k] != 0 {
                            dp[i][j] = dp[i][j].max(dp[j][k]+1);
                        }
                        else {
                            dp[i][j] = 3; 
                        }
                        result = result.max(dp[i][j]); 
                    }
                }
            }
        }
        return result; 
    }
}

struct Solution {}

fn main() {
    assert_eq!(Solution::len_longest_fib_subseq(vec![1,2,3,4,5,6,7,8]), 5); 
}