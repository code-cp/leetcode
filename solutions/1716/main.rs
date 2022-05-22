fn main() {
    assert_eq!(Solution::total_money(20), 96);
}

struct Solution {}

impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let mut result: i32 = 0; 
        let mut deposit: i32 = 0; 
        let mut last_monday: i32 = 0; 
        let mut last_deposit: i32 = 0; 
        let mut cur_day: i32 = 0; 

        while cur_day < n {
            cur_day += 1; 
            if cur_day % 7 == 1 {
                deposit = last_monday + 1; 
                last_monday = deposit; 
            }
            else {
                deposit = last_deposit + 1; 
            }
            result += deposit; 
            last_deposit = deposit; 
        }
        result 
    }
}
