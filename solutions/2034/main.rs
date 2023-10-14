use std::collections::{HashMap, BTreeMap, HashSet}; 

struct StockPrice { 
    latest_timestamp: i32, 
    // key is timestamp, value is price 
    time_hm: HashMap<i32, i32>, 
    // key is price, value is timestamps for that price  
    price_hm: BTreeMap<i32, HashSet<i32>>, 
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockPrice {

    fn new() -> Self {
        Self { 
            latest_timestamp: 0, 
            time_hm: HashMap::new(), 
            price_hm: BTreeMap::<i32, HashSet<i32>>::new(), 
        }
    }
    
    fn update(&mut self, timestamp: i32, price: i32) {
        if timestamp > self.latest_timestamp {
            self.latest_timestamp = timestamp;
        }
        
        if let Some(p) = self.time_hm.get_mut(&timestamp) {
            let old_price = *p; 
            *p = price; 
            
            let t = self.price_hm.get_mut(&old_price).unwrap();
            t.remove(&timestamp); 
            if t.is_empty() {
                self.price_hm.remove(&old_price); 
            }

            let t = self.price_hm.entry(price).or_insert(HashSet::new());
            t.insert(timestamp); 
        } else {
            self.time_hm.insert(timestamp, price); 
            let t = self.price_hm.entry(price).or_insert(HashSet::new()); 
            t.insert(timestamp); 
        }
    }
    
    fn current(&self) -> i32 {
        *self.time_hm.get(&self.latest_timestamp).unwrap()
    }
    
    fn maximum(&self) -> i32 {
        // the last entry is max
        *self.price_hm.iter().rev().next().unwrap().0 
    }
    
    fn minimum(&self) -> i32 {
        // the first entry is min 
        *self.price_hm.iter().next().unwrap().0 
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