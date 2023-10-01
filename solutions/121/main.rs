struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_val = i32::MAX; 
        let mut ans = 0; 
        for p in prices {
            ans = ans.max(p - min_val); 
            if p < min_val {
                min_val = p; 
            } 
        }
        ans 
    }
}