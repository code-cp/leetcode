use std::collections::HashMap; 
impl Solution {
    pub fn find_substring_in_wrapround_string(p: String) -> i32 {
        let mut dp: HashMap<char, i32> = HashMap::new(); 
        let mut pre = 'a'; 
        let mut k: i32 = 0; 
        p.chars().enumerate().for_each(|(i, ch)| {
            // in rust -25 % 26 = -25 
            if (ch as i32 - pre as i32 + 26) % 26 == 1 {
                k += 1; 
            } else {
                k = 1; 
            }
            pre = ch; 
            dp.insert(ch, *dp.get(&ch).unwrap_or(&0).max(&k)); 
        }); 
        dp.values().sum() 
    }
}


struct Solution {}

fn main() {
    assert_eq!(Solution::find_substring_in_wrapround_string("zab".to_string()), 6);
}