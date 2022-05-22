// ref https://leetcode.com/problems/strong-password-checker/discuss/1497854/Rust-Solution-using-Dijkstra's-Algorithm-(156-ms-85.3-MB)-and-BFS-(18-ms-6.7-MB)

use std::collections::BinaryHeap;
use std::cmp::Reverse;

const MINLEN: usize = 6; 
const MAXLEN: usize = 20; 

#[derive(Clone, Copy, PartialOrd, PartialEq, Eq, Ord, Debug)]
struct State {
    cost: Reverse<usize>,
    idx: usize,
    num_chars: usize,
    has_lower: bool,
    has_upper: bool,
    has_digit: bool,
    sec_last: char, 
    last: char, 
}

impl State {
    fn new(cost: Reverse<usize>, idx: usize, num_chars: usize, 
        has_lower: bool, has_upper: bool, has_digit: bool, 
        sec_last: char, last: char
    ) -> State {
        State { cost, idx, num_chars, has_lower, has_upper, has_digit, sec_last, last }
    }
    
    fn calc_hash(&self) -> usize {
        let mut res = self.idx;
        res *= 21;
        res += self.num_chars;
        res *= 2;
        res += self.has_lower as usize;
        res *= 2;
        res += self.has_upper as usize;
        res *= 2;
        res += self.has_digit as usize;
        res *= 1+2*256;
        res += self.sec_last as usize;
        res += self.last as usize;
        res
    }
}

fn inc_rev(x: Reverse<usize>) -> Reverse<usize> {
    Reverse(x.0+1)
}

fn add_new_state(s: &mut [Option<usize>], h: &mut BinaryHeap<State>, state: State) {
    let hash = state.calc_hash();
    let should_insert = match s[hash] {
        None => true,
        Some(c) => state.cost.0 < c
    };
    if should_insert {
        s[hash] = Some(state.cost.0);
        h.push(state);
    }
}

fn add_char(mut s: &mut [Option<usize>], mut h: &mut BinaryHeap<State>, state: State, 
        ch: char, new_cost: Reverse<usize>, new_idx: usize) -> bool {
    let has_lower = state.has_lower || ch.is_ascii_lowercase();
    let has_upper = state.has_upper || ch.is_ascii_uppercase();
    let has_digit = state.has_digit || ch.is_ascii_digit();
    if (state.sec_last != state.last || state.last != ch) && state.num_chars < MAXLEN {
        add_new_state(&mut s, &mut h, State::new(new_cost, new_idx, 
            state.num_chars+1, 
            has_lower, has_upper, has_digit, 
            state.last, ch));
        true
    } else { false }
}

fn change_char(mut s: &mut [Option<usize>], mut h: &mut BinaryHeap<State>, chars: &[char], state: State, ch: char) -> bool {
    if ch == chars[state.idx] || (state.idx+1 < chars.len() && ch == chars[state.idx+1]) {
        return false;
    }

    add_char(&mut s, &mut h, state, ch, inc_rev(state.cost), state.idx+1)
}

fn insert_char(mut s: &mut [Option<usize>], mut h: &mut BinaryHeap<State>, chars: &[char], state: State, ch: char) -> bool {
    if state.idx < chars.len() && ch == chars[state.idx] {
        return false;
    }
    
    add_char(&mut s, &mut h, state, ch, inc_rev(state.cost), state.idx)
}

impl Solution {
    pub fn strong_password_checker(password: String) -> i32 {
        let chars: Vec<char> = password.chars().collect();
        
        let mut min_cost: Vec<Option<usize>> = vec![None; (chars.len()+1)*21*2*2*2*(1+2*256)];
        let mut heap: BinaryHeap<State> = BinaryHeap::new();
        
        add_new_state(&mut min_cost, &mut heap, State::new(Reverse(0), 0, 0, false, false, false, '?', '?'));
        
        while let Some(state) = heap.pop() {
            if let Some(c) = min_cost[state.calc_hash()] {
                if c < state.cost.0 {
                    continue;
                }
            }
            
            if state.idx == chars.len() && state.num_chars >= MINLEN && state.has_lower && state.has_upper && state.has_digit {
                return state.cost.0 as i32;
            }
            
            if state.idx < chars.len() {
                //Edge type 1 (i.e. change nothing)
                add_char(&mut min_cost, &mut heap, state, chars[state.idx], state.cost, state.idx+1);
                
                //Edge type 2 (i.e. delete character)
                add_new_state(&mut min_cost, &mut heap, State::new(inc_rev(state.cost), 
                    state.idx+1, state.num_chars, 
                    state.has_lower, state.has_upper, state.has_digit, 
                    state.sec_last, state.last));
                
                //Edge type 4 (i.e. replace char): lowercase
                for ch in 'a'..='z' {
                    if change_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
                }
                //Edge type 4: uppercase
                for ch in 'A'..='Z' {
                    if change_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
                }
                //Edge type 4: digit
                for ch in '0'..='9' {
                    if change_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
                }
            }
            
            //Edge type 3 (i.e. insert char): lowercase
            for ch in 'a'..='z' {
                if insert_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
            }
            //Edge type 3: uppercase
            for ch in 'A'..='Z' {
                if insert_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
            }
            //Edge type 3: digit
            for ch in '0'..='9' {
                if insert_char(&mut min_cost, &mut heap, &chars, state, ch) { break; }
            }
        }
        return 0; //Should never happen
    }
}

struct Solution {}

fn main() {
    let password = "a".to_string();
    let result = Solution::strong_password_checker(password); 
    assert_eq!(result, 5); 
}