impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        let mask: Vec<i32> = words
            .iter()
            .map(|word| {
                word.chars()
                    .fold(0, |acc, c| acc | 1 << (c as u8 - 'a' as u8))
            })
            .collect(); 

        let mut ans = 0; 
        for i in 0..mask.len() {
            for j in i+1..mask.len() {
                if mask[i] & mask[j] == 0 {
                    ans = ans.max(words[i].len() * words[j].len())
                }
            }
        }

        ans as i32 
    }
}