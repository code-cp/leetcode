impl Solution {
    pub fn count_palindromic_subsequences(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        // dp table 
        let mut dp = vec![vec![0; n]; n]; // dp[i][j] = # of palindromic subsequences in s[i..j] 
        // init 
        for i in 0..n {
            dp[i][i] = 1;
        } 
        // traverse 
        for l in 1..n {
            for i in 0..n-l {
                let j = i+l;
                if s[i] != s[j] {
                    // simple case when both ends are unequal 
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1];
                } else {
                    // when both ends are equal, need to check whether there are 
                    // char in middle equal to end  
                    let mut left = i+1; 
                    let mut right = j-1; 
                    while left <= right && s[left] != s[i] {
                        left += 1; 
                    }
                    while left <= right && s[right] != s[i] {
                        right -= 1; 
                    } 
                    if left > right {
                        // simple case, no char equal to end 
                        dp[i][j] = (2*dp[i+1][j-1] + 2) % 1000000007; 
                    } else if left == right {
                        // only one char equal to end 
                        dp[i][j] = (2*dp[i+1][j-1] + 1) % 1000000007;
                    } else {
                        // more than one char equal to end 
                        dp[i][j] = 2*dp[i+1][j-1] - dp[left+1][right-1];
                    }
                }
                // NOTE, need to handle update < 0 case 
                dp[i][j] = if dp[i][j] >= 0 {dp[i][j] % 1000000007} else {dp[i][j] + 1000000007}; 
            }
        }
        dp[0][n-1]  
    }
}

struct Solution {} 

fn main() {
    assert_eq!(6, Solution::count_palindromic_subsequences("bccb".to_string())); 
    assert_eq!(539524363, Solution::count_palindromic_subsequences("dddcabadcbabccdadccbcabcdacdadcbbbcadaabcddccbcadaddbdbdacbcccddabbbcbcdccdaadabadacacbdbbbadcdaaabb".to_string())); 
    println!("Pass test cases!"); 
}