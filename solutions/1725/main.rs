struct Solution {}

impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut max_len: i32 = i32::MIN; 
        let mut result: i32 = 0; 
        let mut min_side: i32 = 0; 
        rectangles.iter().for_each(|r| {
            min_side = r[0].min(r[1]); 
            if max_len < min_side {
                max_len = min_side; 
                result = 1; 
            } 
            else if max_len == min_side {
                result += 1; 
            }
        });
        return result; 
    }
}

fn main() {
    assert_eq!(Solution::count_good_rectangles(vec![vec![5,8],vec![3,9],vec![5,12],vec![16,5]]), 3); 
}

