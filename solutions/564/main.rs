struct Solution {}

impl Solution {
    pub fn nearest_palindromic(n: String) -> String {
        let str_len = n.chars().count() as u32; 
        let mut candidates = Vec::new(); 
        candidates.push((10_i64.pow(str_len) + 1).to_string()); 
        candidates.push((10_i64.pow(str_len-1) - 1).to_string()); 
        let prefix: String = n.chars().into_iter().take(((str_len+1)/2) as usize).collect();
        let prefix: i64 = prefix.parse::<i64>().unwrap();  
        for i in vec![(prefix-1).to_string(), prefix.to_string(), (prefix+1).to_string()].into_iter() {
            let mut half;
            if str_len % 2 == 0 {
                half = i.to_owned();  
            } else {
                half = i.chars().into_iter().take(((str_len+1)/2 - 1) as usize).collect(); 
            }
            half = half.chars().rev().collect(); 
            let mut result = i.to_owned(); 
            result.push_str(&half); 
            candidates.push(result);
        }
        candidates.retain(|x| !x.eq(&n));
        candidates.sort_by_key(|x| ((x.parse::<i64>().unwrap() - n.parse::<i64>().unwrap()).abs(), x.parse::<i64>().unwrap()));
        candidates[0].to_owned()
    }
}

fn main() {
    assert_eq!(Solution::nearest_palindromic("123".to_string()), "121".to_string()); 
}