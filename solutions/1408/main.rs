impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut ret = vec![]; 
        for i in 0..words.len() {
            let word = &words[i]; 
            for j in 0..words.len() {
                if i == j {
                    continue; 
                }
                let word2 = &words[j];
                if word2.contains(word.as_str()) {
                    ret.push(word.clone());
                    break; 
                }
            }
        }
        ret 
    }
}