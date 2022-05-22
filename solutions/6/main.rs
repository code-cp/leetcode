
struct Solution {}

// ref https://leetcode-cn.com/problems/zigzag-conversion/solution/rustiterator-shi-ge-hao-dong-xi-by-pathogen/
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let num_rows = num_rows as usize; 
        let mut rows = vec![String::new(); num_rows]; 
        let iter = (0..num_rows).chain((1..num_rows-1).rev()).cycle(); 
        iter.zip(s.chars()).for_each(|(r, c)| rows[r].push(c)); 
        rows.into_iter().collect()
    }
}

fn main() {
    assert_eq!(Solution::convert("PAYPALISHIRING".to_string(), 3), "PAHNAPLSIIGYIR".to_string());
}