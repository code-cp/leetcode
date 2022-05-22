impl Solution {
    pub fn backtracking(n: &i32, steps: &i32, bitmask: &u16, valid: &mut i32) -> i32 {
        // base case 
        if steps == n {
            return *valid; 
        }

        for i in 0..10 {
            if bitmask >> i & 1 == 1 {
                continue;  
            }
            if i == 0 {
                Solution::backtracking(n, &(*steps + 1), &(*bitmask | 1 << i), valid);
            } else {
                *valid += 1;
                Solution::backtracking(n, &(*steps + 1), &(*bitmask | 1 << i), valid);
            }
        }

        return *valid; 
    }
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        let mut result = 1;
        Solution::backtracking(&n, &0, &0, &mut result); 
        return result; 
    }
}

struct Solution {}

fn main() {
    assert_eq!(91, Solution::count_numbers_with_unique_digits(2));
    assert_eq!(1, Solution::count_numbers_with_unique_digits(0));
}