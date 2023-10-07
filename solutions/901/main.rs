use std::collections::VecDeque; 

struct StockSpanner {
    num_stack: VecDeque<i32>, 
    cnt_stack: VecDeque<i32>, 
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {

    fn new() -> Self {
        Self {
            num_stack: VecDeque::new(), 
            cnt_stack: VecDeque::new(), 
        }
    }
    
    fn next(&mut self, price: i32) -> i32 {
        let mut res = 1; 
        if self.num_stack.len() == 0 {
            self.num_stack.push_back(price);
            self.cnt_stack.push_back(res); 
            return res; 
        }
        while self.num_stack.len() > 0 && price >= *self.num_stack.back().unwrap() {
            let cnt = self.cnt_stack.pop_back().unwrap(); 
            res += cnt; 
            self.num_stack.pop_back(); 
        }
        self.cnt_stack.push_back(res); 
        self.num_stack.push_back(price); 
        res 
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */