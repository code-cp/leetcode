impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        words.iter().fold(String::new(), |st, w| st + &w[..1]) == s 
    }
}