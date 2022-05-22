use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut hash_map: HashMap<String, i32> = HashMap::new(); 
        for w in (s1 + " " + &s2).split_whitespace() {
            if hash_map.contains_key(w) {
                *hash_map.get_mut(w).unwrap() += 1; 
            } 
            else {
                hash_map.insert(w.to_string(), 1); 
            }
        }
        let mut result: Vec<String> = Vec::new(); 
        for (key, val) in hash_map.iter() {
            if *val == 1 {
                result.push(key.to_string()); 
            }
        }
        return result; 
    }
}

fn main() {
    let s1: String = "this apple is sweet".to_string(); 
    let s2: String = "this apple is sour".to_string();
    assert_eq!(Solution::uncommon_from_sentences(s1, s2), vec!["sour", "sweet"]); 
}

