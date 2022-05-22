// ref https://github.com/jlkiri/rust-data-structures/blob/master/src/stack.rs
pub struct Stack<T> {
    stack: Vec<T>,
  }
  
  impl<T> Stack<T> {
    pub fn new() -> Self {
      Stack { stack: Vec::new() }
    }
  
    pub fn len(&self) -> usize {
      self.stack.len()
    }
  
    pub fn pop(&mut self) -> Option<T> {
      self.stack.pop()
    }
  
    pub fn push(&mut self, item: T) {
      self.stack.push(item)
    }
  
    pub fn is_empty(&self) -> bool {
      self.stack.is_empty()
    }
  
    pub fn peek(&self) -> Option<&T> {
      self.stack.last()
    }
}

struct Solution {}

impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
            let mut stack: Stack<char> = Stack::new();
            let mut result = String::with_capacity(word.len());
            for i in 0..word.len() {
                stack.push(word.chars().nth(i).unwrap()); 
                if word.chars().nth(i).unwrap() == ch {
                    let n = stack.len(); 
                    for _j in 0..n {
                        let w = stack.pop().unwrap();
                        result.push(w); 
                    }
                    for j in n..word.len() {
                        result.push(word.chars().nth(j).unwrap()); 
                    }
                    return result; 
                }
            }
            return word; 
        }
}

fn main() {
    assert_eq!(Solution::reverse_prefix("abcdefd".to_string(), 'd'), "dcbaefd".to_string()); 
}