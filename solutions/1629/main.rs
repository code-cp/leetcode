fn main() {
    assert_eq!(Solution::slowest_key(vec![9,29,49,50], "cbcd".to_string()), 'c');
}

struct Solution {}

impl Solution {
    pub fn slowest_key(release_times: Vec<i32>, keys_pressed: String) -> char {
        let mut result = 'a';
        let mut max_time = 0; 
        let mut time; 
        let keys_vec: Vec<char> = keys_pressed.chars().collect(); 
        for i in 0..release_times.len() {
            if i == 0 {
                time = release_times[i];
            }
            else {
                time = release_times[i] - release_times[i-1];
            }
            if time > max_time {
                max_time = time; 
                result = keys_vec[i]; 
            }
            else if time == max_time {
                if result < keys_vec[i] {
                    result = keys_vec[i]; 
                }
            }
        }
        result
    }
}
