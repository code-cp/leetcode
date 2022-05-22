struct Solution {}

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
}

impl Trie {
    pub fn new() -> Trie {
        Trie {
            root: TrieNode::new_root(), 
        }
    }

    pub fn insert(&mut self, word: String) {
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
            cur_node.is_end = true; 
        } else {
            // insert new word 
            for letter in unmatched..char_list.len() {
                // println!("insert {} into {}", char_list[letter], cur_node.value.unwrap_or_default()); 
                cur_node.insert(char_list[letter], false); 
                cur_node = cur_node.children.get_mut(&char_list[letter]).unwrap(); 
            }
            cur_node.is_end = true; 
        }
    }

    pub fn search(&mut self, word: String) -> bool {
        let mut cur_node = &mut self.root; 
        let char_list: Vec<char> = word.chars().collect(); 

        for letter in 0..char_list.len() {
            if !cur_node.children.contains_key(&char_list[letter]) {
                return false; 
            }
            else {
                cur_node = cur_node.children.get_mut(&char_list[letter]).unwrap(); 
            }
        }
        // println!("search {} is end {}", cur_node.value.unwrap(), cur_node.is_end);
        return cur_node.is_end; 
    }

    pub fn search_word(&mut self, word: String) -> bool {
        for i in 1..word.len() {
            let sub_str = word[..i].to_string();
            // println!("search {}", sub_str);
            if !self.search(sub_str) {
                return false; 
            }
        }
        return true; 
    }
}

impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        let mut my_trie = Trie::new(); 
        for w in words.iter() {
            my_trie.insert(w.to_string()); 
        }
        let mut result = "".to_string(); 
        for w in words.iter() {
            if my_trie.search_word(w.to_string()) {
                if w.len() > result.len() {
                    result = w.to_string(); 
                }
                else if w.len() == result.len() {
                    if w.to_string() < result {
                        result = w.to_string(); 
                    }
                }
            }
        }
        return result; 
    }
}

fn main() {
    let mut my_trie = Trie::new(); 
    my_trie.insert("a".to_string()); 
    my_trie.insert("banana".to_string()); 
    my_trie.insert("app".to_string()); 
    my_trie.insert("appl".to_string()); 
    my_trie.insert("ap".to_string()); 
    my_trie.insert("apply".to_string()); 
    my_trie.insert("apple".to_string()); 
    println!("is banana in the trie? {}", my_trie.search_word("banana".to_string())); 
    println!("is apple in the trie? {}", my_trie.search_word("apple".to_string())); 
}