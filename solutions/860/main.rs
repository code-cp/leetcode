use std::collections::HashMap; 

impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut change: HashMap<i32, i32> = HashMap::new(); 
        for b in bills {
            if b == 5 {
                change.entry(5).and_modify(|val| *val += 1).or_insert(1); 
            } else {
                if change.entry(5).or_insert(0) == &mut 0 {
                    return false; 
                }
                if b == 10 {
                    change.entry(5).and_modify(|val| *val -= 1); 
                    change.entry(10).and_modify(|val| *val += 1).or_insert(1); 
                } else {
                    // b == 20
                    if change.entry(10).or_insert(0) >= &mut 1 {
                        change.entry(10).and_modify(|val| *val -= 1); 
                        change.entry(5).and_modify(|val| *val -= 1); 
                    } else {
                        if change.entry(5).or_insert(0) >= &mut 3 {
                            change.entry(5).and_modify(|val| *val -= 3); 
                        } else {
                            return false; 
                        }
                    }
                }
            }
        }
        return true; 
    }
}

// fn main() {
//     assert_eq!(Solution::lemonade_change(vec![5,5,5,10,20]), true);
// }