use std::collections::HashMap; 

pub struct TrieNode {
    value: Option<char>, 
    is_end: bool, 
    children: HashMap<char, TrieNode>, 
}

impl TrieNode {
    pub fn new(c: char, is_end: bool) -> TrieNode {
        TrieNode {
            value: Option::Some(c), 
            is_end: is_end, 
            children: HashMap::new(), 
        }
    }

    pub fn new_root() -> TrieNode {
        TrieNode {
            value: Option::None, 
            is_end: false, 
            children: HashMap::new(), 
        }
    }

    pub fn check(self, c: char) -> bool {
        self.value == Some(c)
    }

    pub fn insert(&mut self, c: char, is_end: bool) {
        self.children.insert(c, TrieNode::new(c, is_end)); 
    }
}

struct Trie {
    root: TrieNode, 
    word_count: i32, 
}

impl Trie {
    pub fn new() -> Trie {
        Trie {
            root: TrieNode::new_root(), 
            word_count: 0, 
        }
    }

    pub fn insert(&mut self, word: &String) {
        let mut cur_node = &mut self.root; 
        let char_list: Vec<char> = word.chars().collect(); 
        let mut unmatched = 0; 

        for letter in 0..char_list.len() {
            if cur_node.children.contains_key(&char_list[letter]) {
                cur_node = cur_node.children.get_mut(&char_list[letter]).unwrap(); 
            }
            else {
                unmatched = letter; 
                break; 
            }
            unmatched = letter + 1; 
        }

        if unmatched == char_list.len() {
            if !cur_node.is_end {
                self.word_count += 1;
            }
            cur_node.is_end = true; 
        } else {
            // insert new word 
            for letter in unmatched..char_list.len() {
                // println!("insert {} into {}", char_list[letter], cur_node.value.unwrap_or_default()); 
                cur_node.insert(char_list[letter], false); 
                cur_node = cur_node.children.get_mut(&char_list[letter]).unwrap(); 
            }
            self.word_count += 1;
            cur_node.is_end = true; 
        }
    }
}

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        let codes = vec![".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
            ".-..","--","-.","---",".--.","--.-",".-.","...",
            "-","..-","...-",".--","-..-","-.--","--.."];
        let mut my_trie = Trie::new(); 
        for word in words.iter() {
            let input = word
                       .chars()
                       .map(|c| codes[c as usize - 'a' as usize])
                       .fold(String::from(""), |mut acc, c| {
                        acc.push_str(&c);
                        acc 
                       });
            my_trie.insert(&input); 
        }
        my_trie.word_count
    }
}

struct Solution {}

fn main() {
    assert_eq!(Solution::unique_morse_representations(vec![String::from("gin"), String::from("zen"), String::from("gig"), String::from("msg")]), 2);
}