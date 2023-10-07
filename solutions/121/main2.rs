struct Solution; 

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0; 
        let mut min = prices[0]; 
        prices.iter().skip(1).for_each(
            |&v| {
                min = min.min(v); 
                ans = ans.max(v - min); 
            }
        ); 
        ans
    }
}