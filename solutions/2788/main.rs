struct Solution {}

impl Solution {
    pub fn split_words_by_separator(words: Vec<String>, separator: char) -> Vec<String> {
        words
            .iter()
            .flat_map(|s| s.split(separator).collect::<Vec<_>>())
            .map(|s| s.to_string() )
            .filter(|s| !s.is_empty() )
            .collect::<Vec<_>>()
    }
}

fn main() {
    Solution::split_words_by_separator(
        vec![
            "one.two.three".to_string(),
            "four.five".to_string(),
            "six".to_string(),
        ],
        '.',
    );
}
