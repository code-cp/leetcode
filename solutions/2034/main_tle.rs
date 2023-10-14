use std::collections::HashMap; 

struct StockPrice {
    latest_price: i32, 
    latest_timestamp: i32, 
    hm: HashMap<i32, i32>, 
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockPrice {

    fn new() -> Self {
        Self { 
            latest_price: 0, 
            latest_timestamp: 0, 
            hm: HashMap::new(), 
        }
    }
    
    fn update(&mut self, timestamp: i32, price: i32) {
        // NOTE, use >= instead of >
        if timestamp >= self.latest_timestamp {
            self.latest_timestamp = timestamp;
            self.latest_price = price;
        }
        
        // update the entry of a hashmap if it exists, if not create this entry
        self.hm.entry(timestamp).and_modify(|value| {*value = price}).or_insert(price); 
    }
    
    fn current(&self) -> i32 {
        self.latest_price 
    }
    
    fn maximum(&self) -> i32 {
        *self.hm.values().max().unwrap_or(&self.latest_price)
    }
    
    fn minimum(&self) -> i32 {
        *self.hm.values().min().unwrap_or(&self.latest_price) 
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice::new();
 * obj.update(timestamp, price);
 * let ret_2: i32 = obj.current();
 * let ret_3: i32 = obj.maximum();
 * let ret_4: i32 = obj.minimum();
 */