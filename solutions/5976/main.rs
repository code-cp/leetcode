fn main() {
    assert_eq!(Solution::check_valid(vec![vec![1,2,3],vec![3,1,2],vec![2,3,1]]), true);
}

struct Solution {}

impl Solution {
    pub fn check_valid(matrix: Vec<Vec<i32>>) -> bool {
        let n = matrix.len();
        for i in 0..n {
            let mut record_row = vec![0; n];
            let mut record_col = vec![0; n];
            for j in 0..n {
                record_row[(matrix[i][j]-1) as usize] = 1;
                record_col[(matrix[j][i]-1) as usize] = 1;
            }
            let sum: i64 = record_row.iter().sum();
            if sum != (n as i64) {
                return false;
            }
            let sum: i64 = record_col.iter().sum();
            if sum != (n as i64) {
                return false;
            }
        }
        return true;
    }
}
