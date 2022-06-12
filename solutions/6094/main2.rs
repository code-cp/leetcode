use std::collections::HashMap;
impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        let first_letters = ideas.as_slice().into_iter().map(|s| s.as_bytes()[0]).collect::<Vec<_>>();
        let mut groups = HashMap::new(); 
        for (i, f) in first_letters.into_iter().enumerate() {
            let key = &ideas[i][1..]; 
            *groups.entry(key).or_insert(0) |= 1 << (f - b'a'); 
        }
        let mut count: i64 = 0; 
        let mut cnt = vec![vec![0; 26]; 26]; 
        for (_, value) in groups.iter() {
            for i in 0..26 {
                if *value >> i & 1 == 0 {
                    for j in 0..26 {
                        if *value >> j & 1 == 1 {
                            cnt[i][j] += 1; 
                        }
                    }
                }  
            }
        }
        for (_, value) in groups.iter() {
            for i in 0..26 {
                if *value >> i & 1 == 1 {
                    for j in 0..26 {
                        if *value >> j & 1 == 0 {
                            count += cnt[i][j] as i64; 
                        }
                    }
                }  
            }
        }
        count  
    }
}

struct Solution {}

fn main() {
    let ideas = vec!["coffee".to_string(), "donuts".to_string(), "time".to_string(), "toffee".to_string()]; 
    assert_eq!(Solution::distinct_names(ideas), 6); 
}

