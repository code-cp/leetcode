use std::collections::HashMap;

// So the dp[i] is made of 3 parts:

// dp[i - 1]
// (1) * (i - prev[s[i]][-1])
// (-1) * (prev[s[i]][-1] - prev[s[i]][-2])
impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        let mut dp = vec![0; s.len()]; 
        let mut total = 0; 
        let mut last0: HashMap<char, i32> = HashMap::new(); 
        let mut last1: HashMap<char, i32> = HashMap::new(); 
        for (i, c) in s.chars().enumerate() {
            total += (i as i32 - *last0.entry(c).or_insert(-1)) - (*last0.entry(c).or_insert(-1) - *last1.entry(c).or_insert(-1));
            dp[i] = total; 
            *last1.entry(c).or_insert(-1) = *last0.entry(c).or_insert(-1);
            *last0.entry(c).or_insert(-1) = i as i32; 
        }
        dp.iter().sum()
    }
}