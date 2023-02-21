struct Solution {}

use std::iter::FromIterator;
impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        // step1 construct 
        // step2 check 

        let n = lcp.len(); 
        let mut my_chars = vec!['?'; n];
        let mut next_char = 'a'; 
        
        for i in 0..n {
            if my_chars[i] == '?' {
                if next_char as u32 > 'z' as u32 {
                    // no more alphabets available 
                    return "".to_string(); 
                }
                // fill in next smallest char
                my_chars[i] = next_char; 
                // fill in the same chars based on lcp 
                for j in i+1..n {
                    if lcp[i][j] > 0 {
                        my_chars[j] = my_chars[i]; 
                    }
                }
                next_char = std::char::from_u32(next_char as u32 + 1).unwrap(); 
            }
        }
        
        // if s[i] == s[j] => lcp[i][j] = lcp[i+1][j+1] + 1
        // if s[i] != s[j] => lcp[i][j] = 0
        for i in 0..n {
            if my_chars[i] == my_chars[n-1] {
                if !(lcp[i][n-1] == 1 && lcp[n-1][i] == 1) {
                    return "".to_string();
                }
            }
            else {
                if !(lcp[i][n-1] == 0 && lcp[n-1][i] == 0) {
                    return "".to_string();
                }
            }
        }
        for i in 0..n-1 {
            for j in 0..n-1 {
                if my_chars[i] == my_chars[j] {
                    if lcp[i][j] != lcp[i+1][j+1] + 1 {
                        return "".to_string();
                    }
                }
                else {
                    if lcp[i][j] != 0 {
                        return "".to_string();
                    }
                }
            }
        }
        
        String::from_iter(my_chars) 
    }
}

fn main() {
    let lcp = vec![vec![4, 0, 2, 0], vec![0, 3, 0, 1], vec![2, 0, 2, 0], vec![0, 1, 0, 1]];
    println!("{:?}", Solution::find_the_string(lcp)); 
}