use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        let mut result = vec![]; 
        let mut pq = BinaryHeap::new(); 
        if a > 0 {
            pq.push((a, 'a')); 
        }
        if b > 0 {
            pq.push((b, 'b')); 
        }
        if c > 0 {
            pq.push((c, 'c')); 
        }

        let mut max_count: i32 = 0; 
        let mut pre_alpha = 'a'; 
        loop {
            if let Some((count, alpha)) = pq.pop() {
                if count == 0 {
                    return result.iter().collect(); 
                }
                result.push(alpha); 
                max_count += 1; 
                pq.push((count-1, alpha)); 
                pre_alpha = alpha; 
            } 

            if max_count == 2 {
                if let Some((count, alpha)) = pq.pop() { 
                    if count == 0 {
                        return result.iter().collect(); 
                    }
                    if alpha != pre_alpha {
                        result.push(alpha); 
                        pq.push((count-1, alpha)); 
                    }
                    else {
                        if pq.is_empty() {
                            return result.iter().collect();
                        }
                        if let Some((sec_count, sec_alpha)) = pq.pop() {
                            if sec_count == 0 {
                                return result.iter().collect();
                            }
                            result.push(sec_alpha); 
                            pq.push((sec_count-1, sec_alpha)); 
                        }
                        pq.push((count, alpha)); 
                    }
                }
                max_count = 0; 
            }
        }
    }
}

fn main() {
    let a = 7; 
    let b = 1;
    let c = 0; 
    assert_eq!(Solution::longest_diverse_string(a, b, c).len(), "aabaa".len()); 
}