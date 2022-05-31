use std::collections::HashMap; 
impl Solution {
    pub fn dfs(adj: &HashMap<char, Vec<char>>, visited: &mut HashMap<char, bool>, stack: &mut Vec<char>, cur: char) -> bool {
        if visited.contains_key(&cur) {
            return *visited.get(&cur).unwrap();
        }
        *visited.entry(cur).or_insert(false) = true;
        for next in adj.get(&cur).unwrap_or(&vec![]).iter() {
            if Solution::dfs(adj, visited, stack, *next) {
                return true; 
            }
        }
        *visited.entry(cur).or_insert(false) = false;
        stack.push(cur);
        return false; 
    }
    pub fn alien_order(words: Vec<String>) -> String {
        // init adjacency list 
        let mut adj = HashMap::new(); 
        words.iter().for_each(|word| {
            for c in word.chars() {
                adj.entry(c).or_insert(vec![]);
            }
        });
        // build adjacency list 
        for i in 0..words.len()-1 {
            let word1 = words[i].chars().collect::<Vec<char>>();
            let word2 = words[i+1].chars().collect::<Vec<char>>();
            let mut j = 0;
            for (c1, c2) in word1.iter().zip(word2.iter()) {
                if c1 != c2 {
                    adj.get_mut(c1).unwrap().push(*c2);
                    break;
                }
                j += 1;
            }
            // check violation 
            if j == word2.len() && word1.len() > word2.len() {
                return "".to_string();
            }
        } 
        // dfs 
        let mut visited = HashMap::new();
        let mut stack = vec![];
        for c in adj.keys() {
            if Solution::dfs(&adj, &mut visited, &mut stack, *c) {
                return "".to_string();
            }
        }
        stack.iter().rev().map(|c| c.to_string()).collect::<Vec<String>>().join("")
    }
}

struct Solution {}

fn main() {
    let words = vec!["wrt".to_string(),"wrf".to_string(),"er".to_string(),"ett".to_string(),"rftt".to_string()]; 
    assert_eq!("wertf".to_string(), Solution::alien_order(words));
}