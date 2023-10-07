struct Solution; 

// |(max_profit, min_price), &price| ...: Defines the closure that takes the current accumulator value (max_profit, min_price) and the next element &price.

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.iter().fold(
            (0, i32::MAX), 
            |(max_profit, min_price), &price| 
            (max_profit.max(price - min_price), min_price.min(price))
        ).0 
    }
}