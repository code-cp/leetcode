impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        let mut ans = 0; 
        for i in left..=right {
            let w = &words[i as usize]; 
            if "aeiou".contains(w.chars().next().unwrap()) && 
            "aeiou".contains(w.chars().last().unwrap()) {
                ans += 1;
            }
        }
        ans 
    }
}