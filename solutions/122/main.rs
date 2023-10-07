struct Solution; 

use std::collections::VecDeque;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut stack = VecDeque::with_capacity(n);
        let mut ans = 0; 

        for i in 0..n {
            if stack.len() > 0 && prices[i] > *stack.back().unwrap() {
                ans += prices[i] - *stack.back().unwrap(); 
                // pop is optional 
                // stack.pop_back();
            } 
            stack.push_back(prices[i]);
        } 

        ans 
    }
}