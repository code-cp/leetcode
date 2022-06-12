// TLE 
use std::collections::HashMap;
impl Solution {
    pub fn count_common(n1: i32, n2: i32) -> i32 {
        let mut count = 0; 
        let mut n = n1 & n2; 
        while n != 0 {
            if n & 1 == 1 {
                count += 1;
            }
            n >>= 1;
        }
        count 
    }
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        let first_letters = ideas.as_slice().into_iter().map(|s| s.as_bytes()[0]).collect::<Vec<_>>();
        let mut groups = HashMap::new(); 
        for (i, f) in first_letters.into_iter().enumerate() {
            let key = &ideas[i][1..]; 
            *groups.entry(key).or_insert(0) |= 1 << (f - b'a'); 
        }
        let mut count: i64 = 0; 
        for (key1, value1) in groups.iter() {
            for (key2, value2) in groups.iter() {
                if *key1 == *key2 {
                    continue;
                }
                let c = Solution::count_common(*value1, *value2); 
                let num = (value1.count_ones() as i32 - c) * (value2.count_ones() as i32 - c);
                count += num as i64; 
            }
        }
        return count; 
    }
}

struct Solution {}

fn main() {
    let ideas = vec!["coffee".to_string(), "donuts".to_string(), "time".to_string(), "toffee".to_string()]; 
    assert_eq!(Solution::distinct_names(ideas), 6); 
}

