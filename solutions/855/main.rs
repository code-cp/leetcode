use std::collections::BTreeSet;

struct ExamRoom {
    seats: BTreeSet<i32>, 
    capacity: i32, 
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ExamRoom {

    fn new(n: i32) -> Self {
        ExamRoom {
            seats : BTreeSet::new(),
            capacity: n,
        }
    }
    
    fn seat(&mut self) -> i32 {
        // check if len is 0 
        if self.seats.len() == 0 {
            self.seats.insert(0); 
            return 0; 
        }

        let (mut left, mut right) = (0, 0); 
        let mut max_dist = i32::MIN; 
        let mut pre = 0; 
        let mut pick = 0; 
        for (i, item) in self.seats.iter().enumerate() {
            // handle first seat 
            if i == 0 && *item != 0 {
                if *item - pre > max_dist {
                    left = pre; 
                    right = *item; 
                    max_dist = right - left; 
                }
            } else {
                if (*item - pre) / 2 > max_dist {
                    left = pre; 
                    right = *item; 
                    max_dist = (right - left) / 2; 
                    pick = left + max_dist; 
                }
            }
            pre = *item; 
        }
        // handle last seat 
        if pre != self.capacity - 1 {
            if self.capacity - 1 - pre > max_dist {
                left = pre; 
                right = self.capacity - 1; 
                max_dist = right - left; 
                pick = right; 
            }
        }
        self.seats.insert(pick); 
        return pick;  
    }
    
    fn leave(&mut self, p: i32) {
        self.seats.remove(&p); 
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom::new(n);
 * let ret_1: i32 = obj.seat();
 * obj.leave(p);
 */